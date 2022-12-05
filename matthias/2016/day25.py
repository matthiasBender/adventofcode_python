from day23 import Command, Execution, read_input


def is_pattern(lst: list[int]) -> bool:
    return all(x == 0 for x in lst[::2]) and all(x == 1 for x in lst[1::2])


def try_a(a: int, commands: list[Command]) -> bool:
    exec = Execution(commands, registers={"a": a, "b": 0, "c": 0, "d": 0})
    result = exec.run(max_output=10)
    return is_pattern(result)


commands: list[Command] = read_input("day25.dat")
for a in range(1_000):
    if try_a(a, commands):
        print("Solution:", a)
        break
