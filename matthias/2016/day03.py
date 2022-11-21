import re
import numpy as np


def read_input():
    pattern = "(\\d+)\\s+(\\d+)\\s+(\\d+)"
    with open("day03.dat") as f:
        result = []
        for line in f.readlines():
            (s1, s2, s3) = re.search(pattern, line).groups()
            result.append([int(s1), int(s2), int(s3)])
        return np.array(result)


def count_triangles(input) -> int:
    return np.logical_and(
        np.logical_and(
            (input[:, 0] + input[:, 1]) > input[:, 2],
            (input[:, 2] + input[:, 1]) > input[:, 0]
        ),
        (input[:, 0] + input[:, 2]) > input[:, 1]
    ).sum()


input = read_input()
print("Puzzle 1:", count_triangles(input))

new_order = input.T.reshape(input.shape[0] * 3).reshape((input.shape[0], 3))
print("Puzzle 2:", count_triangles(new_order))
