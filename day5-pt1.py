import sys
from utils import read_input

test_values = ['0, 9 -> 5, 9',
               '8, 0 -> 0, 8',
               '9, 4 -> 3, 4',
               '2, 2 -> 2, 1',
               '7, 0 -> 7, 4',
               '6, 4 -> 2, 0',
               '0, 9 -> 2, 9',
               '3, 4 -> 1, 4',
               '0, 0 -> 8, 8',
               '5, 5 -> 8, 2']

# will takes x-y positions as keys and numbers as values
plot_board = {}


def get_x_and_y(values) -> list[list[int], list[int]]:
    '''
    takes a list of values splits the values into sub arrays and makes necessary adjustments
    return in form of [[[x1, y1], [x2, y2]]]
    '''
    split_values = [[[int(cord.strip()) for cord in xy.split(',')] for xy in value.split(
        '->') if xy != ', '] for value in values]

    return split_values


def max_min(val1, val2):
    start = min([val1, val2])
    end = max([val1, val2]) + 1
    return start, end


def add_horizontal_line(y1, y2, x):
    start, end = max_min(y1, y2)
    for i in range(start, end):
        plot_board[f'{i}-{x}'] = plot_board.get(f'{i}-{x}', 0) + 1


def add_vertical_line(x1, x2, y):
    start, end = max_min(x1, x2)
    for i in range(start, end):
        plot_board[f'{y}-{i}'] = plot_board.get(f'{y}-{i}', 0) + 1


def add_diagonal_line(x1, x2, y1, y2):
    start_x, end_x = max_min(x1, x2)
    start_y, end_y = max_min(y1, y2)
    diagonal_length = (end_x - start_x)
    for i in range(diagonal_length):
        x = start_x + i
        y = start_y + i
        plot_board[f'{y}-{x}'] = plot_board.get(f'{y}-{x}', 0) + 1


def generate_board(sanitized_values: list[list[int], list[int]]):
    for entry in sanitized_values:
        x1, y1 = entry[0]
        x2, y2 = entry[1]
        if x1 != x2 and y1 != y2:
            add_diagonal_line(x1, x2, y1, y2)
        elif x1 != x2:
            add_vertical_line(x1, x2, y1)
        elif y1 != y2:
            add_horizontal_line(y1, y2, x1)


def count_danger_zones():
    count = 0
    for zone_count in plot_board.values():
        if zone_count > 1:
            count += 1
    print(count)


def main():
    values = read_input('input-day-5.txt')
    # values = test_values
    sanitized_values = get_x_and_y(values)
    generate_board(sanitized_values)
    count_danger_zones()
    # print(plot_board)


if __name__ == '__main__':
    sys.exit(main())
