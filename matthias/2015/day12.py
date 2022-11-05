from typing import Any, List
import json
from pprint import pprint

input = json.load(open("day12.json"))


def collect_numbers(input: Any) -> List[int]:
    t = type(input)
    if t == int:
        return [input]
    if t == list:
        return [i for item in input for i in collect_numbers(item)]
    if t == dict:
        return collect_numbers(list(input.values()))
    else:
        return []

print("Rätsel 1: ", sum(collect_numbers(input)))

def collect_numbers_no_red(input: Any) -> List[int]:
    t = type(input)
    if t == int:
        return [input]
    if t == list:
        return [i for item in input for i in collect_numbers_no_red(item)]
    if t == dict:
        if "red" in input.values():
            return []
        return collect_numbers_no_red(list(input.values()))
    else:
        return []

print("Rätsel 2: ", sum(collect_numbers_no_red(input)))
