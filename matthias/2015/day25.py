c_row = 2981
c_col = 3075
start_value = 20151125
factor = 252533
divisor = 33554393



def determine_position(row, col):
    return sum(x for x in range(row + col - 1, 0, -1)) - row + 1


def find_code(position):
    return pow(factor, position - 1, divisor) * start_value % divisor

print("Rätsel 1:", find_code(determine_position(c_row, c_col)))