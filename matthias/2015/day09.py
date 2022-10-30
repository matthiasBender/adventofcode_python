from typing import Mapping, List, Tuple
import re
from collections import defaultdict
from itertools import permutations


def read_input() -> Mapping[str, Mapping[str, int]]:
    pattern = "(\\w+) to (\\w+) = (\\d+)"
    with open("day09.dat") as f:
        result = defaultdict(dict)
        for line in f.readlines():
            (start, end, distance) = re.search(pattern, line).groups()
            result[start][end] = int(distance)
            result[end][start] = int(distance)
        return dict(result)        


input = read_input() 

def calculate_length(route: List[str], distances: Mapping[str, Mapping[str, int]]) -> int:
    return sum(distances[start][end] for (start, end) in zip(route, route[1:]))


def find_shortest_route(distances: Mapping[str, Mapping[str, int]]) -> Tuple[List[str], int]:
    shortest = None
    shortest_length = 0xFFFFFFFFFFFFFFFF
    for route in permutations(input.keys()):
        length = calculate_length(route, distances)
        if length < shortest_length:
            shortest = route
            shortest_length = length
    return shortest, shortest_length


print("Rätsel 1: ", find_shortest_route(input)[1])

def find_longest_route(distances: Mapping[str, Mapping[str, int]]) -> Tuple[List[str], int]:
    longest = None
    longest_length = 0
    for route in permutations(input.keys()):
        length = calculate_length(route, distances)
        if length > longest_length:
            longest = route
            longest_length = length
    return longest, longest_length

print("Rätsel 2: ", find_longest_route(input)[1])
