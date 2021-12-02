import requests
import sys


def getValues(day):
    cookies = {
        'session': '53616c7465645f5fd0344be39f601c03e9a9eb1e2341d2afb745ae8f644d5fcfbb7e619b7154aad8c5cd5aa32513af3b'
    }
    resp = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies)
    strValues = resp.text
    lst = strValues.split('\n')[:-1]
    return lst


def func1(values: list):
    hor = 0
    vert = 0
    for val in values:
        dir, str_force = val.split(' ')

        force = int(str_force)
        if dir == 'forward':
            hor += force
        elif dir == 'up':
            vert -= force
        else:
            vert += force

    return hor * vert


def func2(values: list):
    hor = 0
    vert = 0
    aim = 0
    for val in values:
        dir, str_force = val.split(' ')

        force = int(str_force)
        if dir == 'forward':
            hor += force
            vert += (force * aim)
        elif dir == 'up':
            aim -= force
        else:
            aim += force

    return hor * vert


def main():
    values = getValues()
    output1 = func1(values)
    output2 = func2(values)
    print(f'{output1=}')
    print(f'{output2=}')


if __name__ == '__main__':
    sys.exit(main())