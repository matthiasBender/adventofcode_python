import numpy as np


def read_input():
    with open("day06.dat") as f:
        return np.array([list(line.strip()) for line in f.readlines()])


input = read_input()


def decode_frequencies(input, optimizer=max):
    return "".join(
        optimizer(
            [x for x in zip(*np.unique(input[:, i], return_counts=True))],
            key=lambda x: x[1]
        )[0] for i in range(input.shape[1])
    )


print("Puzzle 1:", decode_frequencies(input))
print("Puzzle 2:", decode_frequencies(input, optimizer=min))
