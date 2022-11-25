import numpy as np

input = "11100010111110100"
input_np = np.array([int(i) for i in input], dtype=bool)

example_checksum = "110010110100"
example_checksum_np = np.array([int(i) for i in example_checksum], dtype=bool)

example_full = "10000"
example_full_np = np.array([int(i) for i in example_full], dtype=bool)


def expand(input, target_size=272):
    zero = np.array([False])
    current = input
    while current.size < target_size:
        current = np.concatenate((
            current,
            zero,
            np.logical_not(current[::-1])
        ))
    return current


def print_bin(array):
    print("".join(str(int(i)) for i in array))


def checksum(array):
    current = array
    while current.size % 2 == 0:
        current = current[::2] == current[1::2]
    return current


print("Solution 1:")
print_bin(checksum(expand(input_np)[:272]))
print("Solution 2:")
print_bin(checksum(expand(input_np, 35651584)[:35651584]))
