import re

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def read_input():
    pattern = "Sue (\\d+): (\\w+): (\\d+), (\\w+): (\\d+), (\\w+): (\\d+)"
    with(open("day16.dat")) as f:
        tuples = [re.search(pattern, line).groups() for line in f.readlines()]
        return [
            (
                int(index), 
                {
                    key1: int(value1),
                    key2: int(value2),
                    key3: int(value3),
                }
            ) for (index, key1, value1, key2, value2, key3, value3) in tuples
        ]


def score_entry(value, target=target):
    return sum(1 for (k, v) in value.items() if target[k] == v)


def find_highest_score(aunts, target=target, score_func=score_entry):
    return max(aunts, key=lambda x: score_func(x[1], target))

aunts = read_input()

print("Rätsel 1:", find_highest_score(aunts))


comparison_funcs = {
    "children": lambda x, y: x == y,
    "cats": lambda x, y: x > y,
    "samoyeds": lambda x, y: x == y,
    "pomeranians": lambda x, y: x < y,
    "akitas": lambda x, y: x == y,
    "vizslas": lambda x, y: x == y,
    "goldfish": lambda x, y: x < y,
    "trees": lambda x, y: x > y,
    "cars": lambda x, y: x == y,
    "perfumes": lambda x, y: x == y,
}


def score_entry_improved(value, target=target, comps=comparison_funcs):
    return sum(1 for (k, v) in value.items() if comparison_funcs[k](v, target[k]))


print("Rätsel 2:", find_highest_score(aunts, score_func=score_entry_improved))