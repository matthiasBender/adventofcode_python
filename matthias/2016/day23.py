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


def print_program(program: list[Command], position: int):
    result = ""
    for i, line in enumerate(program):
        result += "->" if i == position else "  "
        result += str(line) + "\n"
    print(result)


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
                if isinstance(instruction.arg2, str):
                    self.registers[instruction.arg2] = self.deref(instruction.arg1)
            case "inc":
                self.optimized_inc(instruction)
            case "dec":
                self.registers[instruction.arg1] -= 1
            case "jnz":
                if self.deref(instruction.arg1):
                    self.position += self.deref(instruction.arg2) - 1
            case "tgl":
                self.toggle_line(self.position - 1 + self.deref(instruction.arg1))

    def optimized_inc(self, cmd: Command):
        # checking and optimizing for:
        # inc a
        # dec c
        # jnz c -2
        # dec d
        # jnz d -5
        sequence = [
            inst.name for inst in
            self.program[self.position: self.position + 4]
        ]
        if sequence == ["dec", "jnz", "dec", "jnz"]:
            prog = self.program
            pc = self.position - 1
            dec1 = prog[pc + 1].arg1
            dec2 = prog[pc + 3].arg1
            if (
                prog[pc + 2].arg2 == -2 and prog[pc + 4].arg2 == -5
                    and prog[pc + 2].arg1 == dec1
                    and prog[pc + 4].arg1 == dec2
            ):
                self.registers[cmd.arg1] += self.deref(dec1) * self.deref(dec2)
                self.registers[dec1] = 0
                self.registers[dec2] = 0
                self.position += 4
                return
        elif sequence[:2] == ["dec", "jnz"]:
            prog = self.program
            pc = self.position - 1
            dec = prog[pc + 1].arg1
            if prog[pc + 2].arg2 == -2 and prog[pc + 2].arg1 == dec:
                self.registers[cmd.arg1] += self.deref(dec)
                self.registers[dec] = 0
                self.position += 2
                return
        self.registers[cmd.arg1] += 1

    def toggle_line(self, x: int):
        if 0 <= x < len(self.program):
            cmd = self.program[x]
            match cmd.name:
                case "inc":
                    cmd.name = "dec"
                case "dec" | "tgl":
                    cmd.name = "inc"
                case "jnz":
                    cmd.name = "cpy"
                case "cpy":
                    cmd.name = "jnz"

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


def read_input(file_name: str = "day23.dat") -> list[Command]:
    with open(file_name) as f:
        result = []
        for line in f.readlines():
            tokens = line.strip().split(" ")
            result.append(Command(*(to_int(t) for t in tokens)))
        return result


if __name__ == "__main__":
    commands = read_input()
    execution = Execution(commands, registers={
        "a": 7,
        "b": 0,
        "c": 0,
        "d": 0
    })
    execution.run()
    print("Solution 1:", execution.registers["a"])

    execution = Execution(read_input(), registers={
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0
    })
    execution.run()
    print("Solution 2:", execution.registers["a"])
