graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []


def find_all_paths(graph, start, end, path):
    path = path + [start]
    paths = []

    if start == end:
        return [path]

    if start not in graph:
        return []

    for neighbor in graph[start]:
        new_paths = find_all_paths(graph, neighbor, end, path)
        paths.extend(new_paths)

    return paths


paths = find_all_paths(graph, start, end, path)
print("Пути из точки A в точку F: ", *paths)
