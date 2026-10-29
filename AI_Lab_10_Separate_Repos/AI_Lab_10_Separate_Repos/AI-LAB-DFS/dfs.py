def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Reverse keeps traversal order intuitive for this example.
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                stack.append(neighbour)
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
        print("DFS traversal:", " -> ".join(dfs(graph, start)))
