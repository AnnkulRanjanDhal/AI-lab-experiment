from itertools import permutations

def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    best_path = None
    min_cost = float("inf")

    for order in permutations(cities):
        path = [start, *order, start]
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return best_path, min_cost

if __name__ == "__main__":
    n = int(input("Enter number of cities: "))
    print("Enter the cost matrix row by row (space-separated):")
    graph = [list(map(int, input().split())) for _ in range(n)]
    if any(len(row) != n for row in graph):
        print("The matrix must be square.")
    else:
        start = int(input(f"Enter starting city (0 to {n - 1}): "))
        if not 0 <= start < n:
            print("Invalid starting city.")
        else:
            path, cost = travelling_salesman(graph, start)
            print("Optimal path:", " -> ".join(map(str, path)))
            print("Minimum cost:", cost)
