from dataclasses import dataclass, field


@dataclass
class Command:
    name: str
    arg1: str | int
    arg2: str | int | None = None

    def __repr__(self) -> str:
        if self.arg2 is None:
            return f"{self.name} {self.arg1}"
        return f"{self.name} {self.arg1} {self.arg2}"


@dataclass
class Execution:
    program: list[Command]
    position: int = 0
    registers: dict[str, int] = field(default_factory=lambda: {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    })

    def execute_command(self):
        instruction = self.program[self.position]
        self.position += 1

        match instruction.name:
            case "cpy":
                self.registers[instruction.arg2] = self.deref(instruction.arg1)
            case "inc":
                self.registers[instruction.arg1] += 1
            case "dec":
                self.registers[instruction.arg1] -= 1
            case "jnz":
                if self.deref(instruction.arg1):
                    self.position += instruction.arg2 - 1

    def deref(self, arg: str | int) -> int:
        if isinstance(arg, int):
            return arg
        return self.registers[arg]

    def run(self):
        size = len(self.program)
        while self.position < size:
            self.execute_command()


def to_int(s: str) -> int | str:
    try:
        return int(s)
    except ValueError:
        return s


def read_input() -> list[Command]:
    with open("day12.dat") as f:
        result = []
        for line in f.readlines():
            tokens = line.strip().split(" ")
            result.append(Command(*(to_int(t) for t in tokens)))
        return result


commands = read_input()
execution = Execution(commands)
execution.run()
print("Solution 1:", execution.registers["a"])

execution = Execution(commands, registers={
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
})
execution.run()
print("Solution 2:", execution.registers["a"])
