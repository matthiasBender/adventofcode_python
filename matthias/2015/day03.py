import numpy as np

def read_input():
    f = open("./day03.dat")
    result = f.readline().strip()
    f.close()
    return np.array(list(result))


def to_input_directions(input):
    result = []
    for i in input:
        if i == "<":
            result.append([0, -1])
        elif i == ">":
            result.append([0, 1])
        elif i == "^":
            result.append([1, 0])
        elif i == "v":
            result.append([-1, 0])
        else:
            raise ValueError(f"Found unmatched character {i}")
    return np.array(result)

directions = to_input_directions(read_input())
positions = directions.cumsum(axis=0)

print("Rätsel 1: ", np.unique(positions, axis=0).shape[0])

prefixed_directions = np.vstack((np.zeros((2,2), dtype=int), directions))
santas_pos = prefixed_directions[::2].cumsum(axis=0)
robos_pos = prefixed_directions[1::2].cumsum(axis=0)
result2 = np.unique(np.vstack((santas_pos, robos_pos)), axis=0)

print("Rätsel 2: ", result2.shape[0])
