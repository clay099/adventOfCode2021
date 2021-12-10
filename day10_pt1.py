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

bracket_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

incorrect = []
for chunk in values:
    chunk_stack = []
    for bracket in chunk:
        if bracket in brackets.keys():
            chunk_stack.append(bracket)
        else:
            last_open_bracket = chunk_stack.pop()
            if brackets[last_open_bracket] != bracket:
                incorrect.append(bracket)
                break

total = 0
for bracket in incorrect:
    total += bracket_points[bracket]

print(total)
