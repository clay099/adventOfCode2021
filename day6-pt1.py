from utils import read_input

values = read_input('input-day-6.txt')[0].split(',')
values = [int(fish) for fish in values]
# values = [3, 4, 3, 1, 2]


def process_fish(fish):
    if fish > 0:
        return fish - 1, None
    else:
        return 6, 8


def process_day():
    for i in range(len(values)):
        fish = values[i]
        fish_1, fish_2 = process_fish(fish)
        values[i] = fish_1
        if fish_2:
            values.append(fish_2)


for day in range(80):
    process_day()

print(len(values))
