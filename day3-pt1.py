import sys
from utils import read_input


test_values = ['00100',
               '11110',
               '10110',
               '10111',
               '10101',
               '01111',
               '00111',
               '11100',
               '10000',
               '11001',
               '00010',
               '01010', ]


def generate_bin_number(temp_dict, length, is_gamma):
    bin_lst = []
    for idx in range(len(temp_dict)):
        val = temp_dict[idx]
        if is_gamma:
            if val > length:
                bin_lst.append('1')
            else:
                bin_lst.append('0')
        else:
            if val < length:
                bin_lst.append('1')
            else:
                bin_lst.append('0')
    bin_str = ''.join(bin_lst)
    bin_number = int(bin_str, 2)

    return bin_number


def main():
    values = read_input('input-day-3.txt')
    # values = test_values
    temp_dict = {}
    length = len(values)/2
    for value in values:
        for idx, b in enumerate(value):
            if b == '1':
                temp_dict[idx] = temp_dict.get(idx, 0) + 1

    gamma = generate_bin_number(temp_dict, length, True)
    epsilon = generate_bin_number(temp_dict, length, False)
    print(gamma * epsilon)


if __name__ == '__main__':
    sys.exit(main())
