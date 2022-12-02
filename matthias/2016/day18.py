input = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."


def to_bools(input: str) -> list[bool]:
    return [bool(ord(i) - 46) for i in input]


def to_string(row: list[bool]) -> str:
    return "".join(chr(int(i) * 48 + 46) for i in row)


def determine_flag(parents: list[bool], index: int) -> bool:
    if len(parents) < 3:
        return (index == 0 and parents[1]) or (index != 0 and parents[0])
    return parents[0] != parents[2]


def next_row(row: list[bool]) -> list[bool]:
    size = len(row)
    return [determine_flag(row[max(i - 1, 0): min(i + 2, size)], i) for i in range(size)]


def find_target_row(start: list[bool], num_rows: int) -> tuple[list[bool], int]:
    current = start
    result = sum(not i for i in current)
    for _ in range(num_rows - 1):
        current = next_row(current)
        result += sum(not i for i in current)
    return current, result


input_bool = to_bools(input)
print("Solution 1:", find_target_row(input_bool, 40)[1])
print("Solution 2:", find_target_row(input_bool, 400_000)[1])
