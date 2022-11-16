import numpy as np
from gmpy2 import popcount, xmpz

input = np.array([
    1,
    2,
    3,
    7,
    11,
    13,
    17,
    19,
    23,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
])


def find_best(list_of_arr):
    size = 0xFF
    prod = 0xFFFFFFFFFFFFFFFF
    result = []
    for arr in list_of_arr:
        if arr.size < size:
            result = arr
            size = arr.size
            prod = arr.prod()
        elif arr.size == size and arr.prod() < prod:
            result = arr
            prod = arr.prod()
    return result, prod


def generate_smallest_options(arr, solution_size=6):
    size = arr.size
    for i in range(2**arr.size):
        xi = xmpz(i)
        if popcount(xi) == solution_size:
            pattern = list(xi.iter_bits(start=0, stop=size))
            yield arr[pattern]


def filter_target(solutions, target):
    for s in solutions:
        if s.sum() == target:
            yield s


target_size = input.sum() / 3
result = find_best(filter_target(generate_smallest_options(input), target_size))
print("Rätsel 1:", result[1])

new_target = input.sum() // 4
result = find_best(filter_target(generate_smallest_options(input, solution_size=4), new_target))
print("Rätsel 2:", result[1])
