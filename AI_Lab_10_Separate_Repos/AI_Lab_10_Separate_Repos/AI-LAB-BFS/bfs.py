from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append(neighbour)
    return order

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"], "E": ["B"], "F": ["C"]
    }
    start = input("Enter starting node (A-F): ").strip().upper()
    if start not in graph:
        print("Invalid start node.")
    else:
        print("BFS traversal:", " -> ".join(bfs(graph, start)))
