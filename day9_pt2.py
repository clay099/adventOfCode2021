from utils import read_input
from collections import deque


area = [[int(cell) for cell in row] for row in read_input('input-day-9.txt')]
test_values = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
               [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
               [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
               [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
               [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
# area = test_values

num_rows = len(area)
num_columns = len(area[0])
seen = set()


def get_left(i, j):
    count = 0


seen = set()


def get_rep(a, b):
    return f'{a}-{b}'


def test_cell(x, y, basin_queue, starting_position_stack):
    cell = area[x][y]
    if cell is not None:
        if cell != 9:
            basin_queue.append([x, y])
            area[x][y] = None
        else:
            rep = get_rep(x, y)
            if rep not in seen:
                seen.add(rep)
                starting_position_stack.append([x, y])
    return basin_queue


basins = []


def get_basin_size(i, j, starting_position_stack):
    basin_queue = [[i, j]]
    basin_size = -1
    while basin_queue:
        basin_size += 1
        x, y = basin_queue.pop()
        if x > 0:
            basin_queue = test_cell(
                x-1, y, basin_queue, starting_position_stack)
        if x + 1 < num_rows:
            basin_queue = test_cell(
                x+1, y, basin_queue, starting_position_stack)
        if y > 0:
            basin_queue = test_cell(
                x, y-1, basin_queue, starting_position_stack)
        if y + 1 < num_columns:
            basin_queue = test_cell(
                x, y+1, basin_queue, starting_position_stack)
    basins.append(basin_size)


# start with [i,j] and add to list when ever you hit a 9
area[0][0] = None
starting_position_stack = deque([[0, 0]])
while starting_position_stack:
    position = starting_position_stack.popleft()
    get_basin_size(position[0], position[1], starting_position_stack)


sorted_basins = sorted(basins)

largest_basins = sorted_basins[-3:]
print(largest_basins[0]*largest_basins[1]*largest_basins[2])
