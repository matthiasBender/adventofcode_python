from typing import Iterable
import numpy as np
from collections import deque

def read_input():
    raw = np.loadtxt("day12.dat", dtype=np.unicode_)
    result = np.array([[ord(x) for x in row] for row in raw]) - ord("a")
    start = np.where(result == ord("S") - ord("a"))
    end = np.where(result == ord("E") - ord("a"))
    result[start] = 0
    result[end] = 26
    return result, tuple(x[0] for x in start), tuple(x[0] for x in end)


def expand(current_pos: tuple[int, int], shape: tuple[int, int]) -> Iterable[tuple[int, int]]:
    x, y = current_pos
    size_x, size_y = shape
    if x > 0:
        yield (x - 1, y)
    if x < size_x - 1:
        yield (x + 1, y)
    if y > 0:
        yield (x, y - 1)
    if y < size_y - 1:
        yield (x, y + 1)


def find_shortest_path(input, start, end):
    shape = input.shape
    visited = np.zeros(shape, dtype=np.int64) - 1
    visited[start] = 0
    q = deque([start])
    while q:
        current = q.popleft()
        if current == end:
            return visited[end]
        level = input[current]
        for pos in expand(current, shape):
            if visited[pos] == -1 and input[pos] <= level + 1:
                q.append(pos)
                visited[pos] = visited[current] + 1
    return 0xFFFFFF


def find_shortest_overall(input, end):
    return min(find_shortest_path(input, p, end) for p in zip(*np.where(input == 0)))


map, start, end = read_input()
print("Solution 1:", find_shortest_path(map, start, end))
print("Solution 2:", find_shortest_overall(map, end))



