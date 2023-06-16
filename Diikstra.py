import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()
    paths = {start: [start]}  # Словарь для хранения путей

    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            return cost, paths[current]
        for neighbor, edge_cost in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + edge_cost, neighbor))
                if neighbor not in paths or len(paths[current]) + 1 < len(paths[neighbor]):
                    paths[neighbor] = paths[current] + [neighbor]
    return -1, []
