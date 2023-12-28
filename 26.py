from collections import deque

def find_all_paths(graph, start, end):
    # Создаем очередь для поиска в ширину
    queue = deque([(start, [start])])
    all_paths = []

    # Пока очередь не пуста
    while queue:
        current_city, current_path = queue.popleft()

        # Если достигли целевого города, добавляем путь в список путей
        if current_city == end:
            all_paths.append(current_path)
            continue

        # Добавляем в очередь все смежные города с новым путем
        for neighbor in graph[current_city]:
            if neighbor not in current_path:
                queue.append((neighbor, current_path + [neighbor]))

    # Сортируем по кол-ву вершин в пути для выделения потом макс. и мин. путей
    all_paths = sorted(all_paths, key=lambda path: len(path[1]))

    return all_paths, all_paths[0], all_paths[-1]

# Пример использования
if __name__ == '__main__':
    # Задаем граф с расстояниями между городами
    graph = {
        'A': ['B', 'C', 'F'],
        'B': ['C', 'D', 'F', 'A'],
        'C': ['D'],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['E', 'B', 'C']
    }

    start_city = 'A'  # Начальный город
    end_city = 'F'    # Целевой город

    # Находим все возможные маршруты от начального до целевого города
    all_paths, min_path, max_path = find_all_paths(graph, start_city, end_city)

    # Выводим все найденные пути
    for path in all_paths:
        print(' -> '.join(path))
    print('Минимальный путь: ', ' -> '.join(min_path))
    print('Максимальный путь: ', ' -> '.join(max_path))