from utils import read_input
import re
from collections import defaultdict

input = read_input('input-day-14.txt')
test_input = ['NNCB',
              'CH -> B',
              'HH -> N',
              'CB -> H',
              'NH -> C',
              'HB -> C',
              'HC -> B',
              'HN -> C',
              'NN -> C',
              'BH -> H',
              'NC -> B',
              'NB -> B',
              'BN -> B',
              'BB -> N',
              'BC -> B',
              'CC -> N',
              'CN -> C', ]
# input = test_input

result = defaultdict(int)
for i in range(len(input[0])-1):
    result[input[0][i:i+2]] = 1
instrutions = [[chars for chars in values.split(
    ' -> ')]for values in input[1:]]


for step in range(40):
    temp = result.copy()

    for direction in instrutions:
        foundInstances = result[direction[0]]
        if foundInstances:
            key1 = direction[0][0] + direction[1]
            key2 = direction[1] + direction[0][1]
            temp[key1] += foundInstances
            temp[key2] += foundInstances
            temp[direction[0]] -= foundInstances
    result = temp


answer = defaultdict(int)
for key, val in result.items():
    answer[key[0]] += val
    answer[key[1]] += val

# values are in included but not in a pair
first = input[0][0]
last = input[0][-1]
answer[first] += 1
answer[last] += 1

for char in answer:
    answer[char] /= 2


max_ans = 0
min_ans = 1e13
for val in answer.values():
    max_ans = max(val, max_ans)
    min_ans = min(val, min_ans)

print(int(max_ans - min_ans))
