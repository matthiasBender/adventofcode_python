import re
import numpy as np


def read_input():
    pattern = r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)."
    with open("day15.dat") as f:
        positions = []
        max_positions = []
        for line in f.readlines():
            (_, num_pos, pos) = re.search(pattern, line).groups()
            positions.append(int(pos))
            max_positions.append(int(num_pos))
        return np.array(positions, dtype=int), np.array(max_positions, dtype=int)


positions, max_positions = read_input()


def find_all_zeros(positions, max_positions) -> int:
    size = positions.size
    result = 0
    current = (positions + np.arange(1, size + 1)) % max_positions
    while current.sum() > 0:
        current = (current + 1) % max_positions
        result += 1
    return result


print("Solution 1:", find_all_zeros(positions, max_positions))
print("Solution 2:", find_all_zeros(np.append(positions, 0), np.append(max_positions, 11)))
