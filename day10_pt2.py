from utils import read_input

values = read_input('input-day-10.txt')
test_values = ['[({(<(())[]>[[{[]{<()<>>',
               '[(()[<>])]({[<{<<[]>>(',
               '{([(<{}[<>[]}>{[]{[(<()>',
               '(((({<>}<{<{<>}{[]{[]{}',
               '[[<[([]))<([[{}[[()]]]',
               '[{[{({}]{}}([{[{{{}}([]',
               '{<[[]]>}<{[{[{[]{()[[[]',
               '[<(<(<(<{}))><([]([]()',
               '<{([([[(<>()){}]>(<<{{',
               '<{([{{}}[<[[[<>{}]]]>[]]', ]
# values = test_values
brackets = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}


def get_leftover_stack(chunk):
    chunk_stack = []
    for bracket in chunk:
        if bracket in brackets.keys():
            chunk_stack.append(bracket)
        else:
            last_open_bracket = chunk_stack.pop()
            if brackets[last_open_bracket] != bracket:
                return None
    return chunk_stack


def get_closing_stack(stack):
    closing_stack = []
    for bracket in stack[::-1]:
        closing_stack.append(brackets[bracket])
    return closing_stack


bracket_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def calculate_score(closing_stack):
    total = 0
    for bracket in closing_stack:
        total *= 5
        total += bracket_points[bracket]
    return total


closing_list = []
for i, chunk in enumerate(values):
    stack = get_leftover_stack(chunk)
    if stack is None:
        continue
    else:
        closing_list.append(get_closing_stack(stack))

score_list = []
for values in closing_list:
    score_list.append(calculate_score(values))

score_list.sort()
print(score_list[len(score_list)//2])
