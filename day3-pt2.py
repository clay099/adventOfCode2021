import sys
from utils import read_input


test_values = read_input('input-day-3.txt')
# test_values = ['00100',
#    '11110',
#    '10110',
#    '10111',
#    '10101',
#    '01111',
#    '00111',
#    '11100',
#    '10000',
#    '11001',
#    '00010',
#    '01010']


def to_decimal(num):
    return int(num, 2)


def count(values, position):
    zeros = []
    ones = []
    for value in values:
        position_value = value[position]
        if position_value == '0':
            zeros.append(value)
        else:
            ones.append(value)

    return zeros, ones


def recursion(values=test_values, position=0, reverse=False):
    if len(values) == 1:
        return values[0]

    zeros, ones = count(values, position)
    position += 1
    if len(zeros) == len(ones):
        if reverse:
            return recursion(zeros, position, reverse)
        else:
            return recursion(ones, position, reverse)
    elif len(zeros) > len(ones):
        if reverse:
            return recursion(ones, position, reverse)
        else:
            return recursion(zeros, position, reverse)
    else:
        if reverse:
            return recursion(zeros, position, reverse)
        else:
            return recursion(ones, position, reverse)


def main():
    oxygen = recursion()
    co2 = recursion(reverse=True)

    print(to_decimal(oxygen) * to_decimal(co2))


if __name__ == '__main__':
    sys.exit(main())
