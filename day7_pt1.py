from utils import read_input, convert_string_list_to_int
import sys
from statistics import mean

starting_position = convert_string_list_to_int(read_input('input-day-7.txt'))

# test values
# starting_position = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

starting_position.sort()
answer = 0
mean_value = mean(starting_position)

best = sys.maxsize
for i in range(max(starting_position)):
    score = 0
    for val in starting_position:
        movement = abs(val-i)
        score += movement*((movement+1)/2)
    if score < best:
        best = score

print(best)
