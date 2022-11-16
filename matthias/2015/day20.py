from collections import defaultdict
import numpy as np

input = 29_000_000


sizes = 20_000

# goal: x + sum(factors(x)) + 1 >= input / 10


def presents_for_house(x):
    factors = np.arange(x / 2, dtype=int) + 1
    return 10 * (x + factors[x % factors == 0].sum())


for house in range(665_000, 750961):
    if presents_for_house(house) >= input:
        print("Rätsel 1:", house)
        break
    if house % 1000 == 0:
        print(house, presents_for_house(house))


def lazy_presents(x):
    factors = np.arange(x / 50 - 1, x / 2, dtype=int) + 1
    return 11 * (x + factors[x % factors == 0].sum())


for house in range(665_000, 750961):
    if lazy_presents(house) >= input:
        print("Rätsel 2:", house)
        break
    if house % 1000 == 0:
        print(house, lazy_presents(house))
