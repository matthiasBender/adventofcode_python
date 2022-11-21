import re
import numpy as np


def read_input():
    pattern = r'\[|\]'
    with open("day07.dat") as f:
        result = []
        for line in f.readlines():
            tokens = re.split(pattern, line.strip())
            result.append(["#".join(tokens[::2]), "#".join(tokens[1::2])])
        return np.array(result)


def contains_abba(s: str) -> bool:
    return any(
        c1 == c4 and c2 == c3 and c1 != c2
        for c1, c2, c3, c4 in zip(s, s[1:], s[2:], s[3:])
    )


def count_valid_tls(input):
    abbarize = np.vectorize(contains_abba)
    abbas = abbarize(input)
    return np.logical_and(
        abbas[:, 0],
        np.logical_not(abbas[:, 1])
    ).sum()


input = read_input()
print("Puzzle 1:", count_valid_tls(input))


def find_all_inverted_abas(s: str) -> list[str]:
    return [
        c2 + c1 + c2
        for c1, c2, c3 in zip(s, s[1:], s[2:])
        if c1 == c3 and c1 != c2
    ]


def count_valid_ssl(input):
    return sum(
        any(s in row[1] for s in find_all_inverted_abas(row[0]))
        for row in input
    )


print("Puzzle 2:", count_valid_ssl(input))
