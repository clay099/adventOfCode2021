import requests
import datetime


def get_values(day):
    cookies = {
        'session': '53616c7465645f5fd0344be39f601c03e9a9eb1e2341d2afb745ae8f644d5fcfbb7e619b7154aad8c5cd5aa32513af3b'
    }
    resp = requests.get(
        f'https://adventofcode.com/2021/day/{day}/input', cookies=cookies)
    str_values = resp.text

    with open(f'input-day-{day}.txt', 'w') as f:
        f.write(str_values)


def read_input(filename):
    '''Read Input'''
    try:
        with open(filename) as f:
            return [l.strip() for l in f.readlines() if l.strip() != '']
    except FileNotFoundError:
        date = datetime.datetime.utcnow()
        day = date.strftime('%d').lstrip('0')
        get_values(day)
        with open(filename) as f:
            return [l.strip() for l in f.readlines() if l.strip() != '']
