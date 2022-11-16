import numpy as np
from itertools import permutations


def read_input():
    data = np.loadtxt("day17.dat", dtype=int)
    data.sort()
    return np.flip(data)

input = read_input()
target = 150


def generate_selectors(filter_size=None):
    for i in range(2**20):
        pattern = np.array([bool(i & (1<<n)) for n in range(20)])
        if filter_size is None or pattern.sum() == filter_size:
            yield pattern


def count_matches(input, target, filter_size=None):
    return sum(1 for p in generate_selectors(filter_size=filter_size) if input[p].sum() == target)

print("Rätsel 1:", count_matches(input, target))


def find_minimum_matching_size(input, target):
    return min(p.sum() for p in generate_selectors() if input[p].sum() == target)


minimum = find_minimum_matching_size(input, target)
print("minimum:", minimum)
print("Rätsel 2:", count_matches(input, target, filter_size=minimum))

