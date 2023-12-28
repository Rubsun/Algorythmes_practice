from collections import deque

def is_cyclic(graph: dict):
    queue = deque([(0, graph[0])])
    visited = [False] * len(graph)

    while queue:
        v, edges = queue.popleft()
        visited[v] = True

        for edge in edges:
            if visited[edge] == True:
                return True
            queue.append((edge, graph[edge]))

    return False


# Задаем граф (ациклический)
graphic = [
    [1, 2],
    [3, 4], 
    [5],
    [],
    [],
    [],
]

print(is_cyclic(graphic))
