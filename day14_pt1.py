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

result = input[0]
instrutions = [[chars for chars in values.split(
    ' -> ')]for values in input[1:]]
test_answers = {0: 'NCNBCHB',
                1: 'NBCCNBBBCBHCB',
                2: 'NBBBCNCCNBBNBNBBCHBHHBCHB',
                3: 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'}


for step in range(10):
    temp = {}
    for i in range(len(result)):
        temp[i] = {'starting': result[i], 'addition': []}

    for direction in instrutions:
        foundIdxs = [x.start() for x in re.finditer(
            '(?={0})'.format(re.escape(direction[0])), result)]
        if len(foundIdxs):
            for idx in foundIdxs:
                temp[idx]['addition'].append(
                    direction[1])
    updated_result = ''
    for i in range(len(result)):
        index_result = temp[i]['starting']
        if len(temp[i]['addition']):
            index_result += ''.join(temp[i]['addition'])
        updated_result += index_result
    result = updated_result

answer = defaultdict(int)
for char in result:
    answer[char] += 1

print(answer)

max_ans = 0
min_ans = 1e9
for val in answer.values():
    if val > max_ans:
        max_ans = val
    if val < min_ans:
        min_ans = val
print(max_ans - min_ans)
