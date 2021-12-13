from utils import read_input
from collections import defaultdict


values = read_input('input-day-12.txt')
tests_values = ['start-A',
                'start-b',
                'A-c',
                'A-b',
                'b-d',
                'A-end',
                'b-end']
values = tests_values

graph = {}
for directions in values:
    path = directions.split('-')
    graph[path[0]] = {*graph.get(path[0], []), path[1]}
    graph[path[1]] = {*graph.get(path[1], []), path[0]}


def check_visits(counter_dict, key):
    return counter_dict[key] < 2


def move_node(node='start', visited=defaultdict(int), count=0):
    for linked_node in graph[node]:
        if linked_node.isupper():
            count = move_node(linked_node, visited.copy(), count)
        else:
            visited_copy = visited.copy()
            if linked_node == 'end':
                count += 1
            elif linked_node not in ['start'] and check_visits(visited, linked_node):
                visited_copy[linked_node] += 1
                count = move_node(linked_node, visited_copy, count)

    return count


total = move_node()
print(total)
