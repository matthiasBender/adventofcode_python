def read_input() -> list[tuple[str, int]]:
    with open("day09.dat") as f:
        result = []
        for line in f.readlines():
            direct, steps = line.strip().split(" ")
            result.append((direct, int(steps)))
        return result


def move_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail
    tx, ty = tail
    hx, hy = head
    if tx < hx:
        tx += 1
    elif tx > hx:
        tx -= 1
    if ty < hy:
        ty += 1
    elif ty > hy:
        ty -= 1
    return (tx, ty)


def move_rope(command: tuple[str, int], rope: list[tuple[int, int]], visited: set[tuple[int, int]]) -> list[tuple[int, int]]:
    direction, steps = command
    length = len(rope)
    current_rope = rope.copy()
    for _ in range(steps):
        match direction:#
            case "R":
                current_rope[0] = (current_rope[0][0] + 1, current_rope[0][1])
            case "L":
                current_rope[0] = (current_rope[0][0] - 1, current_rope[0][1])
            case "U":
                current_rope[0] = (current_rope[0][0], current_rope[0][1] + 1)
            case "D":
                current_rope[0] = (current_rope[0][0], current_rope[0][1] - 1)
        for i, head, tail in zip(range(length), current_rope, current_rope[1:]):
            current_rope[i + 1] = move_tail(head, tail)
        visited.add(current_rope[-1])
    return current_rope


def run_full_rope(commands: list[tuple[str, int]], length=2) -> int:
    rope = [(0, 0)] * length
    visited = set()
    for cmd in commands:
        rope = move_rope(cmd, rope, visited)
    return len(visited)


commands = read_input()
print("Solution 1:", run_full_rope(commands))
print("Solution 2:", run_full_rope(commands, length=10))














