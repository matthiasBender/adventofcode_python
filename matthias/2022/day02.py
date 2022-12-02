def read_input() -> list[tuple[str, str]]:
    with open("day02.dat") as f:
        return [tuple(line.strip().split(" ")) for line in f.readlines()]


def score_round(enemy: str, own: str) -> int:
    result = 1 + ord(own) - ord("X")
    e_num = 1 + ord(enemy) - ord("A")
    if result == e_num:
        return result + 3
    elif result == e_num + 1 or result == e_num - 2:
        return result + 6
    return result


input = read_input()
print("Solution 1:", sum(score_round(*i) for i in input))


def score_round_related(enemy: str, own: str) -> int:
    e_num = ord(enemy) - ord("A")
    match own:
        case "X": 
            return 0 + (e_num - 1) % 3 + 1
        case "Y":
            return 3 + e_num + 1
        case "Z":
            return 6 + (e_num + 1) % 3 + 1


print("Solution 2:", sum(score_round_related(*i) for i in input))
