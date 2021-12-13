from utils import read_input

values = read_input('input-day-12.txt')
tests_values = ['start-A',
                'start-b',
                'A-c',
                'A-b',
                'b-d',
                'A-end',
                'b-end']
# values = tests_values

graph = {}
for directions in values:
    path = directions.split('-')
    graph[path[0]] = {*graph.get(path[0], []), path[1]}
    graph[path[1]] = {*graph.get(path[1], []), path[0]}


def move_node(node='start', visited=set(['start']), count=0):
    if node == 'end':
        return count + 1

    for linked_node in graph[node]:
        if linked_node.isupper():
            count = move_node(linked_node, visited.copy(), count)
        else:
            if linked_node not in visited:
                visited_copy = visited.copy()
                if linked_node != 'end':
                    visited_copy.add(linked_node)
                count = move_node(linked_node, visited_copy, count)
    return count


total = move_node()
print(total)
