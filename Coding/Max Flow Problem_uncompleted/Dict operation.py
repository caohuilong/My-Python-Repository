graph = {
    'x': {'a': 2.0, 'b': 1.0},
    'c': {'y': 2.0},
    'b': {'c': 0, 'd': 1.0},
    'y': {},
    'd': {'e': 1.0},
    'e': {'y': 1.0},
    'a': {'c': 2.0}
}

def BFS(graph, key):
    path = []
    path.append(key)
    while graph[key] != None:

        for k in graph[key].keys():
            if graph[key][k] != 0:
                BFS(graph, k)
                path
        res.append(path)


res = []
for
BFS(graph, 'x')
