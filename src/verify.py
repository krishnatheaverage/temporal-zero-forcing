#!/usr/bin/env python3
"""Exhaustive checks for small temporal zero-forcing instances.

The implementation follows the paper convention exactly:

* colors persist;
* eligibility at time t is evaluated from the blue set at time t-1;
* all eligible targets are added simultaneously;
* exactly one forcing round is performed per temporal layer.
"""

from __future__ import annotations

import csv
import itertools
import json
from pathlib import Path
from typing import Iterable, Literal, Sequence

Edge = tuple[int, int]
Layer = tuple[Edge, ...]
Semantics = Literal["layer-local", "footprint-constrained"]


def _neighborhoods(n: int, edges: Iterable[Edge]) -> list[set[int]]:
    nbrs = [set() for _ in range(n)]
    for u, v in edges:
        if u == v or not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"invalid edge {(u, v)} for n={n}")
        nbrs[u].add(v)
        nbrs[v].add(u)
    return nbrs


def derived_set(
    n: int,
    layers: Sequence[Layer],
    seeds: Iterable[int],
    semantics: Semantics,
) -> frozenset[int]:
    """Return the final blue set under synchronous temporal forcing."""

    blue = set(seeds)
    if not blue <= set(range(n)):
        raise ValueError("seed outside the vertex set")
    if semantics not in {"layer-local", "footprint-constrained"}:
        raise ValueError(f"unknown semantics: {semantics}")

    footprint = _neighborhoods(n, itertools.chain.from_iterable(layers))
    for layer in layers:
        active = _neighborhoods(n, layer)
        newly_blue: set[int] = set()
        for u in blue:
            reference = active[u] if semantics == "layer-local" else footprint[u]
            white_neighbors = reference - blue
            if len(white_neighbors) != 1:
                continue
            v = next(iter(white_neighbors))
            if v in active[u]:
                newly_blue.add(v)
        blue.update(newly_blue)
    return frozenset(blue)


def temporal_zero_forcing_number(
    n: int, layers: Sequence[Layer], semantics: Semantics
) -> tuple[int, tuple[int, ...]]:
    """Compute the exact number and one optimum seed set by enumeration."""

    for size in range(n + 1):
        for seeds in itertools.combinations(range(n), size):
            if len(derived_set(n, layers, seeds, semantics)) == n:
                return size, seeds
    raise AssertionError("the full vertex set is always feasible")


def static_zero_forcing_number(
    n: int, edges: Iterable[Edge]
) -> tuple[int, tuple[int, ...]]:
    """Compute ordinary static zero forcing and return one optimum witness."""

    nbrs = _neighborhoods(n, edges)
    for size in range(n + 1):
        for seeds in itertools.combinations(range(n), size):
            blue = set(seeds)
            while True:
                newly_blue = {
                    next(iter(nbrs[u] - blue))
                    for u in blue
                    if len(nbrs[u] - blue) == 1
                }
                if not newly_blue:
                    break
                blue.update(newly_blue)
            if len(blue) == n:
                return size, seeds
    raise AssertionError("the full vertex set is always feasible")


def alternating_path(n: int) -> tuple[Layer, Layer]:
    first = tuple((u, u + 1) for u in range(0, n - 1, 2))
    second = tuple((u, u + 1) for u in range(1, n - 1, 2))
    return first, second


def alternating_even_cycle(n: int) -> tuple[Layer, Layer]:
    if n < 4 or n % 2:
        raise ValueError("alternating_even_cycle requires even n >= 4")
    first = tuple((u, u + 1) for u in range(0, n, 2))
    second = tuple((u, (u + 1) % n) for u in range(1, n, 2))
    return first, second


def binomial_temporal_tree(lifetime: int) -> tuple[int, tuple[Layer, ...]]:
    """Each existing vertex receives one fresh child in every layer."""

    vertices = [0]
    next_vertex = 1
    layers: list[Layer] = []
    for _ in range(lifetime):
        old_vertices = tuple(vertices)
        layer: list[Edge] = []
        for u in old_vertices:
            v = next_vertex
            next_vertex += 1
            vertices.append(v)
            layer.append((u, v))
        layers.append(tuple(layer))
    return len(vertices), tuple(layers)


def serialized_star(n: int) -> tuple[Layer, ...]:
    if n < 2:
        raise ValueError("serialized_star requires n >= 2")
    return tuple(((0, leaf),) for leaf in range(1, n))


def completed_serialized_clique(n: int) -> tuple[Layer, ...]:
    """Serialize center-leaf edges, then all remaining leaf-leaf edges."""

    layers = list(serialized_star(n))
    layers.extend(((u, v),) for u, v in itertools.combinations(range(1, n), 2))
    return tuple(layers)


def run_checks() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for n in range(1, 21):
        layers = alternating_path(n)
        ll, ll_seed = temporal_zero_forcing_number(n, layers, "layer-local")
        fc, fc_seed = temporal_zero_forcing_number(n, layers, "footprint-constrained")
        ll_formula = n // 4 + 1
        fc_formula = (n + 2) // 3
        assert ll == ll_formula, (n, ll, ll_formula)
        assert fc == fc_formula, (n, fc, fc_formula)
        rows.extend(
            [
                {
                    "family": "alternating_path",
                    "n": n,
                    "lifetime": 2,
                    "semantics": "layer-local",
                    "computed": ll,
                    "formula": ll_formula,
                    "witness": " ".join(map(str, ll_seed)),
                },
                {
                    "family": "alternating_path",
                    "n": n,
                    "lifetime": 2,
                    "semantics": "footprint-constrained",
                    "computed": fc,
                    "formula": fc_formula,
                    "witness": " ".join(map(str, fc_seed)),
                },
            ]
        )

    for n in range(4, 23, 2):
        layers = alternating_even_cycle(n)
        ll, ll_seed = temporal_zero_forcing_number(n, layers, "layer-local")
        fc, fc_seed = temporal_zero_forcing_number(n, layers, "footprint-constrained")
        ll_formula = (n + 3) // 4
        fc_formula = 2 * ((n + 5) // 6)
        assert ll == ll_formula, (n, ll, ll_formula)
        assert fc == fc_formula, (n, fc, fc_formula)
        rows.extend(
            [
                {
                    "family": "alternating_even_cycle",
                    "n": n,
                    "lifetime": 2,
                    "semantics": "layer-local",
                    "computed": ll,
                    "formula": ll_formula,
                    "witness": " ".join(map(str, ll_seed)),
                },
                {
                    "family": "alternating_even_cycle",
                    "n": n,
                    "lifetime": 2,
                    "semantics": "footprint-constrained",
                    "computed": fc,
                    "formula": fc_formula,
                    "witness": " ".join(map(str, fc_seed)),
                },
            ]
        )

    for lifetime in range(1, 5):
        n, layers = binomial_temporal_tree(lifetime)
        ll, ll_seed = temporal_zero_forcing_number(n, layers, "layer-local")
        fc, fc_seed = temporal_zero_forcing_number(n, layers, "footprint-constrained")
        reverse_ll, reverse_seed = temporal_zero_forcing_number(
            n, tuple(reversed(layers)), "layer-local"
        )
        reverse_fc, reverse_fc_seed = temporal_zero_forcing_number(
            n, tuple(reversed(layers)), "footprint-constrained"
        )
        expected_fc = 1 if lifetime == 1 else 2 ** (lifetime - 1)
        assert ll == 1
        assert fc == expected_fc
        assert reverse_ll == expected_fc
        assert reverse_fc == fc
        rows.extend(
            [
                {
                    "family": "binomial_temporal_tree_forward",
                    "n": n,
                    "lifetime": lifetime,
                    "semantics": "layer-local",
                    "computed": ll,
                    "formula": 1,
                    "witness": " ".join(map(str, ll_seed)),
                },
                {
                    "family": "binomial_temporal_tree_forward",
                    "n": n,
                    "lifetime": lifetime,
                    "semantics": "footprint-constrained",
                    "computed": fc,
                    "formula": expected_fc,
                    "witness": " ".join(map(str, fc_seed)),
                },
                {
                    "family": "binomial_temporal_tree_reversed",
                    "n": n,
                    "lifetime": lifetime,
                    "semantics": "layer-local",
                    "computed": reverse_ll,
                    "formula": expected_fc,
                    "witness": " ".join(map(str, reverse_seed)),
                },
                {
                    "family": "binomial_temporal_tree_reversed",
                    "n": n,
                    "lifetime": lifetime,
                    "semantics": "footprint-constrained",
                    "computed": reverse_fc,
                    "formula": expected_fc,
                    "witness": " ".join(map(str, reverse_fc_seed)),
                },
            ]
        )

        if lifetime >= 2:
            footprint_edges = tuple(itertools.chain.from_iterable(layers))
            static, static_seed = static_zero_forcing_number(n, footprint_edges)
            static_formula = n // 4
            assert static == static_formula
            rows.append(
                {
                    "family": "binomial_tree_footprint",
                    "n": n,
                    "lifetime": lifetime,
                    "semantics": "static",
                    "computed": static,
                    "formula": static_formula,
                    "witness": " ".join(map(str, static_seed)),
                }
            )

    for n in range(3, 13):
        layers = serialized_star(n)
        ll, ll_seed = temporal_zero_forcing_number(n, layers, "layer-local")
        fc, fc_seed = temporal_zero_forcing_number(n, layers, "footprint-constrained")
        footprint_edges = tuple(itertools.chain.from_iterable(layers))
        static, static_seed = static_zero_forcing_number(n, footprint_edges)
        assert ll == 1
        assert fc == n - 2
        assert static == n - 2
        rows.extend(
            [
                {
                    "family": "serialized_star",
                    "n": n,
                    "lifetime": n - 1,
                    "semantics": "layer-local",
                    "computed": ll,
                    "formula": 1,
                    "witness": " ".join(map(str, ll_seed)),
                },
                {
                    "family": "serialized_star",
                    "n": n,
                    "lifetime": n - 1,
                    "semantics": "footprint-constrained",
                    "computed": fc,
                    "formula": n - 2,
                    "witness": " ".join(map(str, fc_seed)),
                },
                {
                    "family": "serialized_star_footprint",
                    "n": n,
                    "lifetime": n - 1,
                    "semantics": "static",
                    "computed": static,
                    "formula": n - 2,
                    "witness": " ".join(map(str, static_seed)),
                },
            ]
        )

    for n in range(3, 9):
        layers = completed_serialized_clique(n)
        ll, ll_seed = temporal_zero_forcing_number(n, layers, "layer-local")
        fc, fc_seed = temporal_zero_forcing_number(n, layers, "footprint-constrained")
        footprint_edges = tuple(itertools.chain.from_iterable(layers))
        static, static_seed = static_zero_forcing_number(n, footprint_edges)
        assert ll == 1
        assert fc == n - 1
        assert static == n - 1
        rows.extend(
            [
                {
                    "family": "completed_serialized_clique",
                    "n": n,
                    "lifetime": n * (n - 1) // 2,
                    "semantics": "layer-local",
                    "computed": ll,
                    "formula": 1,
                    "witness": " ".join(map(str, ll_seed)),
                },
                {
                    "family": "completed_serialized_clique",
                    "n": n,
                    "lifetime": n * (n - 1) // 2,
                    "semantics": "footprint-constrained",
                    "computed": fc,
                    "formula": n - 1,
                    "witness": " ".join(map(str, fc_seed)),
                },
                {
                    "family": "completed_serialized_clique_footprint",
                    "n": n,
                    "lifetime": n * (n - 1) // 2,
                    "semantics": "static",
                    "computed": static,
                    "formula": n - 1,
                    "witness": " ".join(map(str, static_seed)),
                },
            ]
        )

    # Exhaust every two-layer temporal graph on four labeled vertices.  Each
    # static edge has four states: absent, first layer, second layer, or both.
    # This independently checks dominance and footprint reversal invariance.
    complete_edges = tuple(itertools.combinations(range(4), 2))
    for states in itertools.product(range(4), repeat=len(complete_edges)):
        layers_lists: list[list[Edge]] = [[], []]
        for edge, state in zip(complete_edges, states):
            if state & 1:
                layers_lists[0].append(edge)
            if state & 2:
                layers_lists[1].append(edge)
        layers = tuple(tuple(layer) for layer in layers_lists)
        ll, _ = temporal_zero_forcing_number(4, layers, "layer-local")
        fc, _ = temporal_zero_forcing_number(4, layers, "footprint-constrained")
        reverse_fc, _ = temporal_zero_forcing_number(
            4, tuple(reversed(layers)), "footprint-constrained"
        )
        assert ll <= fc
        assert fc == reverse_fc

    return rows


def main() -> None:
    rows = run_checks()
    results_dir = Path(__file__).resolve().parents[1] / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    output = results_dir / "verification.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "archive_version": "1.0.0",
        "formula_instances": len(rows),
        "two_layer_schedules": 4096,
        "two_layer_vertices": 4,
        "properties_checked_exhaustively": [
            "layer-local dominance over footprint-constrained forcing",
            "footprint-constrained time-reversal invariance",
        ],
        "status": "passed",
    }
    summary_output = results_dir / "verification_summary.json"
    with summary_output.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
        handle.write("\n")

    print(
        f"Verified {len(rows)} formula instances and 4,096 exhaustive "
        f"two-layer schedules; wrote {output}"
    )


if __name__ == "__main__":
    main()
