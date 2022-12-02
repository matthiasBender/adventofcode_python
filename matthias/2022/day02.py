def read_input() -> list[tuple[str, str]]:
    with open("day02.dat") as f:
        return [tuple(line.strip().split(" ")) for line in f.readlines()]


def score_round(enemy: str, own: str) -> int:
    result = ord(own) - ord("X") + 1
    e_num = ord(enemy) - ord("A")
    return (result - e_num) % 3 * 3 + result


input = read_input()
print("Solution 1:", sum(score_round(*i) for i in input))


def score_round_related(enemy: str, own: str) -> int:
    e_num = ord(enemy) - ord("A")
    s = ord(own) - ord("X")
    return 3 * s + (e_num + s - 1) % 3 + 1


print("Solution 2:", sum(score_round_related(*i) for i in input))
