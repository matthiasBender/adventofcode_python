def read_input():
    with open("day01.dat") as f:
        content = f.read()
        return [[int(y) for y in x.split("\n")] for x in content.split("\n\n") ]


input = read_input()
print("Solution 1:", max(sum(x) for x in input))
print("Solution 2:", sum(sorted((sum(x) for x in input), reverse=True)[:3]))