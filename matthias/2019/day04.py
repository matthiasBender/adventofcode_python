start = 402328
end = 864247


def is_valid(pw: str) -> bool:
    return any(a == b for a, b in zip(pw, pw[1:])) and all(a <= b for a, b in zip(pw, pw[1:]))


def count_in_range(start: int, end: int, check=is_valid):
    return sum(check(str(pw)) for pw in range(start, end + 1))


print("Solution 1:", count_in_range(start, end))


def valid_improved(pw: str) -> bool:
    return (
        all(a <= b for a, b in zip(pw, pw[1:]))
        and any(
            a != x and a != y and a == b
            for a, b, x, y in zip(pw, pw[1:], " " + pw, pw[2:] + " ")
        )
    )


print("Solution 1:", count_in_range(start, end, valid_improved))
