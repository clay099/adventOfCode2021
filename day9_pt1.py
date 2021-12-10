from utils import read_input


area = [[int(cell) for cell in row] for row in read_input('input-day-9.txt')]
test_values = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
               [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
               [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
               [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
               [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
# area = test_values

num_rows = len(area)
num_columns = len(area[0])


def get_smallest_surrounding(i, j):
    options = []
    if i > 0:
        options.append(area[i-1][j])
    if i + 1 < num_rows:
        options.append(area[i+1][j])
    if j > 0:
        options.append(area[i][j-1])
    if j + 1 < num_columns:
        options.append(area[i][j+1])
    return min(options)


lowest = []
for i, row in enumerate(area):
    for j, cell in enumerate(row):
        smallest_surrounding = get_smallest_surrounding(i, j)
        if cell < smallest_surrounding:
            lowest.append(cell)

print(sum([cell + 1 for cell in lowest]))
