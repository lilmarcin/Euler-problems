import math

def number_of_routes(grid_size):
    # n - total number of moves to get to end point(add two side lengths of the grid)
    # quadratic grid => a+a = 2*a
    n = 2 * grid_size
    # Number of moves in one direction (right or down)
    k = grid_size  
    return math.comb(n, k)

grid_size = 20
result = number_of_routes(grid_size)
print(result)
