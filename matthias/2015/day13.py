from typing import Mapping, List
import re
from collections import defaultdict
from itertools import permutations


def read_input() -> Mapping[str, Mapping[str, int]]:
    pattern = "(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."
    with open("day13.dat") as f:
        result = defaultdict(dict)
        for line in f.readlines():
            (person1, gain, weight, person2) = re.search(pattern, line).groups()
            result[person1][person2] = int(weight) if gain == "gain" else -int(weight)
        return dict(result)


def score_happiness(seating: List[str], weights: Mapping[str, Mapping[str, int]]) -> int:
    return sum(
        weights[p1][p2] + weights[p2][p1] for (p1, p2) in zip(seating, seating[1:])
    ) + weights[seating[0]][seating[-1]] + weights[seating[-1]][seating[0]]


def find_optimal_seating(weights: Mapping[str, Mapping[str, int]], score_func) -> int:
    max_happyness = -0xFFFFFFFF
    for seating in permutations(weights.keys()):
        score = score_func(seating, weights)
        if score > max_happyness:
            max_happyness = score
    return max_happyness


input = read_input()
print("Rätsel 1: ", find_optimal_seating(input, score_happiness))


def score_happiness_with_me(seating: List[str], weights: Mapping[str, Mapping[str, int]]) -> int:
    return sum(
        weights[p1][p2] + weights[p2][p1] for (p1, p2) in zip(seating, seating[1:])
    )

print("Rätsel 2: ", find_optimal_seating(input, score_happiness_with_me))
