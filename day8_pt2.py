from utils import read_input

values = read_input('input-day-8.txt')

mapping = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}


def strip_space(string_value):
    return [l.strip() for l in string_value.split(' ') if l.strip() != '']


def get_known(sorted_signals, solved_values):
    for signal in sorted_signals:
        sorted_signal = ''.join(sorted(signal))
        if len(sorted_signal) == 2:
            solved_values[1] = sorted_signal
        elif len(sorted_signal) == 4:
            solved_values[4] = sorted_signal
        elif len(sorted_signal) == 3:
            solved_values[7] = sorted_signal
        elif len(sorted_signal) == 7:
            solved_values[8] = sorted_signal
    return solved_values


def get_three(sorted_signal, solved_values):
    return len(set(sorted_signal) & set(solved_values[1])) == 2


def get_five(sorted_signal, solved_values):
    return len(set(sorted_signal) & set(solved_values[4])) == 3


def get_nine(sorted_signal, solved_values):
    return len(set(sorted_signal) & set(solved_values[4])) == 4


def get_zero(sorted_signal, solved_values):
    return len(set(sorted_signal) & set(solved_values[1])) == 2


def get_other_entries(sorted_signals, solved_values):
    for signal in sorted_signals:
        sorted_signal = ''.join(sorted(signal))
        sorted_signals_len = len(sorted_signal)

        # options include 0,6 & 9
        if sorted_signals_len == 6:
            if get_nine(sorted_signal, solved_values):
                solved_values[9] = sorted_signal
            else:
                if get_zero(sorted_signal, solved_values):
                    solved_values[0] = sorted_signal
                else:
                    solved_values[6] = sorted_signal

        # options include 2,3 & 5
        elif sorted_signals_len == 5:
            if get_three(sorted_signal, solved_values):
                solved_values[3] = sorted_signal
            else:
                if get_five(sorted_signal, solved_values):
                    solved_values[5] = sorted_signal
                else:
                    solved_values[2] = sorted_signal

        # we don't care about other then values as we have already mapped them

    return solved_values


def get_four_digit_value(solved_values, four_digit):
    temp_list = []
    for digit in four_digit:
        sorted_digit = ''.join(sorted(digit))
        value = solved_values[sorted_digit]
        temp_list.append(str(value))

    return int(''.join(temp_list))


def switch_key_value(solved_values):
    temp_dict = {}
    for key, value in solved_values.items():
        temp_dict[value] = key
    return temp_dict


def process_values():
    total = 0
    for line in values:
        signals, four_digit = [strip_space(section)
                               for section in line.split('|')]
        sorted_signals = sorted(signals)
        solved_values = {}
        # we know values for 1,4,7 & 8
        solved_values = get_known(sorted_signals, solved_values)
        # get values for 0,2,3,5,6 & 9
        solved_values = get_other_entries(sorted_signals, solved_values)
        # we currently have keys that a ints and values of strings, we need that reversed for calculation
        solved_values = switch_key_value(solved_values)
        # we have all values so we can calculate
        digit_values = get_four_digit_value(solved_values, four_digit)
        total += digit_values

    print(total)


process_values()
