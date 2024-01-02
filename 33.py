def has_negative_cycle(n, edges):
    # Инициализация массива расстояний
    distance = [float('inf')] * n
    distance[0] = 0

    # Релаксация ребер n-1 раз
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Проверка наличия цикла отрицательного веса
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            return True

    return False

# Пример использования
n = 5
edges = [(0, 1, -1), (1, 2, -2), (2, 3, 1), (3, 1, -3), (4, 0, 2)]

if has_negative_cycle(n, edges):
    print("Граф содержит цикл отрицательного веса.")
else:
    print("Граф не содержит цикл отрицательного веса.")
