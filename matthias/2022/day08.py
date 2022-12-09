import numpy as np


def read_input():
    with open("day08.dat") as f:
        return np.array(
            [list(line.strip()) for line in f.readlines()],
            dtype=np.int8
        )


def check_trees(arr):
    trees = np.zeros(arr.shape, dtype=np.bool_)
    start_row = np.zeros(arr.shape[1], dtype=np.int8) - 1
    for i, row in enumerate(arr):
        sel = row > start_row
        trees[i] = sel
        start_row[sel] = row[sel]
    return trees


def count_all_trees(arr):
    return np.logical_or(
        np.logical_or(
            check_trees(arr),
            check_trees(arr[::-1])[::-1]
        ),
        np.logical_or(
            check_trees(arr.T).T,
            check_trees(arr.T[::-1])[::-1].T
        )
    ).sum()


forest = read_input()
print("Solution 1:", count_all_trees(forest))


def score_direction(height: int, arr):
    trees = arr >= height
    if trees.sum() == 0:
        return trees.size
    return np.where(trees)[0][0] + 1


def calculate_scenic(arr, x, y):
    height = arr[x, y]
    left = score_direction(height, arr[x][:y][::-1])
    right = score_direction(height, arr[x][y + 1:])
    up = score_direction(height, arr[:x, y][::-1])
    down = score_direction(height, arr[x + 1:, y])
    return up * down * left * right


print("Solution 2:", max(
    calculate_scenic(forest, x, y) for x, row in enumerate(forest) for y, _ in enumerate(row)
))
