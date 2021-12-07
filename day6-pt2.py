from utils import read_input
from collections import defaultdict


values = read_input('input-day-6.txt')[0].split(',')
values = [int(fish) for fish in values]
# values = [3, 4, 3, 1, 2]
dict_store = defaultdict(int)
for fish in values:
    dict_store[fish] = dict_store.get(fish, 0) + 1


def process_day():
    new = defaultdict(int)

    # spawn the 0s
    new[8] = dict_store[0]
    new[6] = dict_store[0]

    # tick down the 1 - 8s
    for i in range(1, 9):
        new[i-1] += dict_store[i]

    return new


for day in range(256):
    dict_store = process_day()

print(sum(dict_store.values()))
