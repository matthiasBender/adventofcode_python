from typing import Iterable, Self
import numpy.typing as npt
from dataclasses import dataclass
import numpy as np
from collections import deque
from itertools import permutations


def read_input() -> tuple[npt.NDArray[np.bool_], list[tuple[int, int]]]:
    with open("day24.dat") as f:
        raw = np.array([list(line.strip()) for line in f.readlines()])
        free = raw != '#'
        positions = {}
        for idx, field in np.ndenumerate(raw):
            if field != "#" and field != ".":
                positions[int(field)] = idx
        return free, [x[1] for x in sorted(positions.items(), key=lambda x: x[0])]


labyrinth, targets = read_input()


def find_next_options(position: tuple[int, int], labyrinth: npt.NDArray[np.bool_]) -> Iterable[tuple[int, int]]:
    x, y = position
    if x > 0 and labyrinth[x - 1, y]:
        yield (x - 1, y)
    if x < labyrinth.shape[0] - 1 and labyrinth[x + 1, y]:
        yield (x + 1, y)
    if y > 0 and labyrinth[x, y - 1]:
        yield (x, y - 1)
    if x < labyrinth.shape[1] - 1 and labyrinth[x, y + 1]:
        yield (x, y + 1)


def find_shortest_path(start: tuple[int, int], target: tuple[int, int], labyrinth: npt.NDArray[np.bool_] = labyrinth) -> int:
    found = set([start])
    q = deque([(start, 0)])
    while q:
        current, steps = q.popleft()
        if current == target:
            return steps
        for next_pos in find_next_options(current, labyrinth=labyrinth):
            if next_pos not in found:
                found.add(next_pos)
                q.append((next_pos, steps + 1))
    return -1


def find_path_length(targets: list[tuple[int, int]], known_distances: dict[tuple[tuple[int, int], tuple[int, int]], int], labyrinth: npt.NDArray[np.bool_]) -> int:
    if len(targets) <= 1:
        return 0
    if (targets[0], targets[1]) in known_distances:
        return known_distances[(targets[0], targets[1])] + find_path_length(targets[1:], known_distances, labyrinth)
    else:
        first = find_shortest_path(targets[0], targets[1], labyrinth)
        known_distances[(targets[0], targets[1])] = first
        known_distances[(targets[1], targets[0])] = first
        return first + find_path_length(targets[1:], known_distances, labyrinth)


def find_shortest_path_to_all(targets: list[tuple[int, int]] = targets, labyrinth: npt.NDArray[np.bool_] = labyrinth) -> int:
    start = targets[0]
    remaining = targets[1:]
    known_distances = {}
    return min(
        find_path_length([start] + list(perm), known_distances, labyrinth) for perm in permutations(remaining)
    )


print("Solution 1:", find_shortest_path_to_all())


def find_shortest_roundtrip(targets: list[tuple[int, int]] = targets, labyrinth: npt.NDArray[np.bool_] = labyrinth) -> int:
    start = targets[0]
    remaining = targets[1:]
    known_distances = {}
    return min(
        find_path_length([start] + list(perm) + [start], known_distances, labyrinth) for perm in permutations(remaining)
    )


print("Solution 2:", find_shortest_roundtrip())
