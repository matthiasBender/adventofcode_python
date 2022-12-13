import json
from functools import cmp_to_key
from pprint import pprint

def read_input():
    with open("day13.dat") as f:
        result = []
        pairs = f.read().split("\n\n")
        for pair in pairs:
            first, second = pair.split("\n")
            result.append((json.loads(first), json.loads(second)))
        return result


def compare_lists(left: list[int], right: list[int]) -> int:
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            elif l > r:
                return 1
            else:
                continue
        if isinstance(l, int):
            l = [l]
        if isinstance(r, int):
            r = [r]
        result = compare_lists(l, r)
        if result != 0:
            return result
    return len(left) - len(right)


pairs = read_input()
print("Solution 1:", sum(i + 1 for i in range(len(pairs)) if compare_lists(*pairs[i]) < 0))

sorted_lists = sorted((x for pair in pairs + [([[2]], [[6]])] for x in pair), key=cmp_to_key(compare_lists))
print((sorted_lists.index([[2]]) + 1) * (sorted_lists.index([[6]]) + 1))
