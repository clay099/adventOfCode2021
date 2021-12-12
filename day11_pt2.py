from os import EX_NOUSER
from utils import read_input

input = read_input('input-day-11.txt')

test_input = ['5483143223',
              '2745854711',
              '5264556173',
              '6141336146',
              '6357385478',
              '4167524645',
              '2176841721',
              '6882881134',
              '4846848554',
              '5283751526']
# input = test_input

input = [[int(cell) for cell in row]
         for row in input]

num_rows = len(input)
num_columns = len(input[0])


def get_adjacent(i, j, copy):
    adjacent_stack = []
    if i > 0:
        if copy[i-1][j] < 10:
            adjacent_stack.append([i-1, j])
        if j > 0 and copy[i-1][j-1] < 10:
            adjacent_stack.append([i-1, j-1])
        if j + 1 < num_columns and copy[i-1][j+1] < 10:
            adjacent_stack.append([i-1, j+1])
    if i + 1 < num_rows:
        if copy[i+1][j] < 10:
            adjacent_stack.append([i+1, j])
        if j > 0 and copy[i+1][j-1] < 10:
            adjacent_stack.append([i+1, j-1])
        if j + 1 < num_columns and copy[i+1][j+1] < 10:
            adjacent_stack.append([i+1, j+1])
    if j > 0:
        if copy[i][j-1] < 10:
            adjacent_stack.append([i, j-1])
    if j + 1 < num_columns:
        if copy[i][j+1] < 10:
            adjacent_stack.append([i, j+1])
    return adjacent_stack


def step_cell(i, j, copy):
    cell = copy[i][j]
    cell += 1
    copy[i][j] = cell

    if cell == 10:
        return get_adjacent(i, j, copy)
    return None


def update_input(copy):
    total = 0
    for i, row in enumerate(copy):
        for j in range(num_columns):
            if copy[i][j] > 9:
                input[i][j] = 0
                total += 1
            else:
                input[i][j] = copy[i][j]
    return total


def run_step():
    copy = [[col for col in row] for row in input]
    for i, row in enumerate(copy):
        for j in range(num_columns):
            adjacent_stack = step_cell(i, j, copy)
            while adjacent_stack:
                cords = adjacent_stack.pop()
                new_adjacent_stack = step_cell(cords[0], cords[1], copy)
                if new_adjacent_stack:
                    adjacent_stack.extend(new_adjacent_stack)
    total_step = update_input(copy)
    return total_step


for i in range(1000):
    total = run_step()
    if total == num_columns * num_rows:
        print(i + 1)
        break
