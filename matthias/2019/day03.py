def read_input() -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    with open("day03.dat") as f:
        line1, line2 = f.read().strip().split("\n")
        line1 = [(item[0], int(item[1:])) for item in line1.strip().split(",")]
        line2 = [(item[0], int(item[1:])) for item in line2.strip().split(",")]
        return line1, line2


def to_points(line: list[tuple[str, int]]) -> tuple[set[tuple[int, int]], dict[tuple[int, int], int]]:
    start = (0, 0)
    steps_total = 0
    step_dict = {}
    current = start
    for direction, steps in line:
        for _ in range(steps):
            match direction:
                case "U":
                    current = current[0], current[1] + 1
                case "D":
                    current = current[0], current[1] - 1
                case "R":
                    current = current[0] + 1, current[1]
                case "L":
                    current = current[0] - 1, current[1]
            steps_total += 1
            if current not in step_dict:
                step_dict[current] = steps_total
    return set(step_dict.keys()), step_dict


line1, line2 = read_input()
point_set1, steps1 = to_points(line1)
point_set2, steps2 = to_points(line2)
print("Solution 1:", min(abs(x) + abs(y) for (x, y) in point_set1.intersection(point_set2)))
print("Solution 2:", min(steps1[p] + steps2[p] for p in point_set1.intersection(point_set2)))
