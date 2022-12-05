from day23 import Command, Execution, read_input


commands: list[Command] = read_input("day12.dat")
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
