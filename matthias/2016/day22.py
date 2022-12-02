from typing import Iterable, Self
import re
from dataclasses import dataclass
from itertools import combinations
from collections import deque
import numpy as np
import numpy.typing as npt


@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    available: int
    use_percent: int

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Node) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return self.x ^ self.y

    def empty(self) -> bool:
        return self.used == 0


@dataclass
class ViablePair:
    a: Node
    b: Node

    def is_valid(self: Node) -> bool:
        return not self.a.empty() and self.a != self.b and self.b.available >= self.a.used

    def __repr__(self) -> str:
        return "<" + str(self.a) + ", " + str(self.b) + ">"


@dataclass
class Grid:
    used: npt.NDArray
    available: npt.NDArray
    target: tuple[int, int]
    hole: tuple[int, int] = None

    def __repr__(self) -> str:
        return f"Grid(target={self.target}, hole={self.hole})"

    def __eq__(self, other: Self) -> bool:
        return self.target == other.target and self.hole == other.hole

    def __hash__(self) -> int:
        return hash(self.target) ^ hash(self.hole)

    def move_field(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        new_target = self.target if start != self.target else end
        new_hole = start if end == self.hole else self.hole
        result = Grid(np.copy(self.used), np.copy(self.available), new_target, new_hole)
        amount = result.used[start]
        result.used[start] = 0
        result.used[end] += amount
        result.available[start] += amount
        result.available[end] -= amount
        return result

    def next_holes(self) -> Iterable[Self]:
        if not self.hole:
            self.hole = np.where(self.used == 0)
            self.hole = (self.hole[0][0], self.hole[1][0])
        y, x = self.hole
        available = self.available[y, x]
        if x > 0 and self.used[y, x - 1] <= available:
            yield self.move_field((y, x - 1), (y, x))
        if x < self.used.shape[1] - 1 and self.used[y, x + 1] <= available:
            yield self.move_field((y, x + 1), (y, x))
        if y > 0 and self.used[y - 1, x] <= available:
            yield self.move_field((y - 1, x), (y, x))
        if y < self.used.shape[0] - 1 and self.used[y + 1, x] <= available:
            yield self.move_field((y + 1, x), (y, x))


def read_input():
    pattern = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"
    with open("day22.dat") as f:
        result: list[Node] = []
        for line in f.readlines():
            match = re.search(pattern, line)
            if match:
                result.append(
                    Node(*[int(x) for x in match.groups()])
                )
        return result


nodes = read_input()


def generate_valid_pairs(nodes: list[Node] = nodes) -> Iterable[ViablePair]:
    for a, b in combinations(nodes, 2):
        pair = ViablePair(a, b)
        if pair.is_valid():
            yield pair
        pair = ViablePair(b, a)
        if pair.is_valid():
            yield pair


print("Solution 1:", sum(1 for _ in generate_valid_pairs()))


def to_grid(nodes: list[Node] = nodes) -> Grid:
    max_x = max(node.x for node in nodes) + 1
    max_y = max(node.y for node in nodes) + 1
    used = np.zeros((max_x, max_y), dtype=np.int16)
    available = np.zeros((max_x, max_y), dtype=np.int16)
    for node in nodes:
        used[node.x, node.y] = node.used
        available[node.x, node.y] = node.available
    return Grid(used, available, target=(max_x - 1, 0))


def valid_next_moves(grid: Grid, steps: int, found: set[Grid]) -> Iterable[tuple[Grid, int]]:
    for new_grid in grid.next_holes():
        if new_grid not in found:
            found.add(new_grid)
            yield (new_grid, steps)


def shortest_path(grid: Grid = to_grid()) -> int:
    q = deque([(grid, 0)])
    found = set([grid])
    while q:
        current, steps = q.popleft()
        if current.target == (0, 0):
            return steps
        q.extend(valid_next_moves(current, steps + 1, found))
    return -1


print("Solution 2:", shortest_path())
