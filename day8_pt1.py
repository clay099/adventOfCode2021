from utils import read_input

values = read_input('input-day-8.txt')

mapping = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def strip_space(string):
    return [l.strip() for l in string.split(' ') if l.strip() != '']


def process_values():
    count = 0
    for line in values:
        signal, four_digit = [strip_space(section)
                              for section in line.split('|')]
        for digit in four_digit:
            if mapping.get(len(digit)):
                count += 1

    print(count)


process_values()
