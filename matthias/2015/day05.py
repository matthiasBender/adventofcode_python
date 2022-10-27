def read_input():
    with open("day05.dat") as f:
        return [line.strip() for line in f.readlines()]


def is_nice(str):
    vowels = set(["a", "e", "i", "o", "u"])
    contains_3vowels = len([v for v in str if v in vowels]) >= 3
    contains_doubles = any(first == second for (first, second) in zip(str, str[1:]))
    naughty = ["ab", "cd", "pq", "xy"]
    contains_no_naughties = all(n not in str for n in naughty)
    return contains_3vowels and contains_doubles and contains_no_naughties


input = read_input()

print(is_nice("aaa"))
print(is_nice("ugknbfddgicrmopn"))
print("Rätsel 1: ", len([i for i in input if is_nice(i)]))


def is_nicer(str):
    pairs = list(zip(str, str[1:]))
    contains_double_doubles = any(
        pair in pairs[i + 2:]
        for i, pair in enumerate(pairs[:-2])
    )
    contains_inter_repeat = any(
        first == third for (first, _, third) in zip(str, str[1:], str[2:])
    )
    return contains_double_doubles and contains_inter_repeat


print(is_nicer("aaaa"))
print(is_nicer("qjhvhtzxzqqjkmpb"))
print(is_nicer("xxyxx"))
print(is_nicer("uurcxstgmygtbstg"))
print(is_nicer("ieodomkazucvgmuy"))
print("Rätsel 2: ", len([i for i in input if is_nicer(i)]))
