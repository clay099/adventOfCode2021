
with open('input-day-13.txt') as f:
    values = [l.strip() for l in f.readlines()]
    break_point = values.index('')
    f_sec = values[0: break_point]
    f_sec = [[int(pos) for pos in cords.split(',')] for cords in f_sec]
    s_sec = values[break_point + 1:]
    s_sec = [[val if i == 0 else int(val) for i, val in enumerate(
        inst[11:].split('='))] for inst in s_sec]

test_f_values = [[6, 10],
                 [0, 14],
                 [9, 10],
                 [0, 3],
                 [10, 4],
                 [4, 11],
                 [6, 0],
                 [6, 12],
                 [4, 1],
                 [0, 13],
                 [10, 12],
                 [3, 4],
                 [3, 0],
                 [8, 4],
                 [1, 10],
                 [2, 14],
                 [8, 10],
                 [9, 0]]

test_s_values = [['y', 7], ['x', 5]]

# f_sec, s_sec = test_f_values, test_s_values

max_x = 0
max_y = 0
for cords in f_sec:
    max_x = max(max_x, cords[0]+1)
    max_y = max(max_y, cords[1]+1)

paper = [['.' for i in range(max_x)] for j in range(max_y)]

MARK = '#'


def print_paper(paper_to_print=paper):
    for row in paper_to_print:
        print(row)


for cords in f_sec:
    paper[cords[1]][cords[0]] = MARK


def fold_y(passed_paper, fold_spot):
    bottom = passed_paper[fold_spot+1:]
    top = passed_paper[0:fold_spot]
    folded_paper = [[cell for cell in row]for row in top]
    for i, row in enumerate(bottom):
        for j, cell in enumerate(row):
            if cell == MARK:
                folded_paper[len(folded_paper)-1-i][j] = MARK
    return folded_paper


def fold_x(passed_paper, fold_spot):

    folded_paper = [
        ['.' for i in range(max(fold_spot, len(passed_paper[0])-fold_spot))] for j in range(len(passed_paper))]
    for i, row in enumerate(passed_paper):
        left = row[0:fold_spot]
        right = row[fold_spot+1:]
        for j, cell in enumerate(right):
            if cell == MARK:
                folded_paper[i][j] = MARK
        for j, cell in enumerate(left):
            if cell == MARK:
                folded_paper[i][len(folded_paper[0])-1-j] = MARK
    return folded_paper


def get_total(folded_paper):
    total = 0
    for row in folded_paper:
        for cell in row:
            if cell == MARK:
                total += 1
    print(total)


def part1():
    folded_paper = paper
    fold = s_sec[0]
    if fold[0] == 'x':
        folded_paper = fold_x(folded_paper, fold[1])
    else:
        folded_paper = fold_y(folded_paper, fold[1])
    get_total(folded_paper)


def test():
    folded_paper = paper
    for fold in s_sec:
        if fold[0] == 'x':
            folded_paper = fold_x(folded_paper, fold[1])
        else:
            folded_paper = fold_y(folded_paper, fold[1])
            print_paper(folded_paper)
    get_total(folded_paper)


part1()
