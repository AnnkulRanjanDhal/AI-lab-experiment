import heapq

def a_star(graph, heuristic, start, goal):
    open_heap = [(heuristic[start], start)]
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    parent = {start: None}

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g_score[goal]

        for neighbour, cost in graph[current]:
            tentative = g_score[current] + cost
            if tentative < g_score[neighbour]:
                g_score[neighbour] = tentative
                parent[neighbour] = current
                heapq.heappush(open_heap, (tentative + heuristic[neighbour], neighbour))
    return None, float("inf")

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": []
    }
    heuristic = {"A": 4, "B": 3, "C": 1, "D": 0}
    path, cost = a_star(graph, heuristic, "A", "D")
    if path:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print("No path found")
