from collections import deque

def water_jug(capacity1, capacity2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path

        pour12 = min(a, capacity2 - b)
        pour21 = min(b, capacity1 - a)
        next_states = [
            (capacity1, b), (a, capacity2), (0, b), (a, 0),
            (a - pour12, b + pour12),
            (a + pour21, b - pour21)
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

if __name__ == "__main__":
    result = water_jug(4, 3, 2)
    if result:
        print("Jug states (4-litre jug, 3-litre jug):")
        for state in result:
            print(state)
    else:
        print("No solution found.")
