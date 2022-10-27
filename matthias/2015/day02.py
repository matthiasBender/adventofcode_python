import numpy as np


def read_input():
    f = open("./day02.dat")
    lines = [
        tuple(
            int(i) for i in l.strip().split("x")
        ) for l in f.readlines()
    ]
    f.close()
    return lines

input = read_input()

def calculate_surface(length, width, height):
    ground = length * width
    side = width * height
    front = height * length
    return 2 * (ground + side + front) + min(ground, side, front)


surfaces = sum(calculate_surface(*i) for i in input)
print(f"Rätsel 1: {surfaces}")


def calculate_ribbon_length(length, width, height):
    ground = 2 * (length + width)
    side = 2 * (width + height)
    front = 2 * (height + length)
    return length * width * height + min(ground, side, front)


l = sum(calculate_ribbon_length(*i) for i in input)
print(f"Rätsel 2: {l}")


input = np.array(input)

def calculated_all_surfaces(input):
    grounds = input[:,0] * input[:,1]
    sides = input[:,1] * input[:,2]
    fronts = input[:,0] * input[:,2]
    return 2 * (grounds + sides + fronts) + np.min(np.array([grounds, sides, fronts]), axis=0)

result = calculated_all_surfaces(input).sum()
print(f"Rätsel 1: {result}")

def calculate_ribbons(input):
    grounds = 2 * (input[:,0] + input[:,1])
    sides = 2 * (input[:,1] + input[:,2])
    fronts = 2 * (input[:,0] + input[:,2])
    return input[:,0] * input[:,1] * input[:,2] + np.min(np.array([grounds, sides, fronts]), axis=0)

print(f"Rätsel 2: {calculate_ribbons(input).sum()}")
