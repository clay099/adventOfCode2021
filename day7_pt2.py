from utils import read_input, convert_string_list_to_int
import sys
from collections import defaultdict

starting_position = convert_string_list_to_int(read_input('input-day-7.txt'))

# test values
# starting_position = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

starting_position.sort()
answer = 0
med = starting_position[len(starting_position)//2]

for val in starting_position:
    answer += abs(val - med)

print(answer)
