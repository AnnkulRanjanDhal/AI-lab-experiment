def objective_function(x):
    # Maximum is at x = 5, where f(x) = 100.
    return -4 * (x - 5) ** 2 + 100

def hill_climbing(start, step_size, max_iterations):
    current = start
    for _ in range(max_iterations):
        current_value = objective_function(current)
        left = current - step_size
        right = current + step_size
        if objective_function(left) > current_value:
            current = left
        elif objective_function(right) > current_value:
            current = right
        else:
            break
    return current, objective_function(current)

if __name__ == "__main__":
    start = float(input("Enter starting value: "))
    step = float(input("Enter step size: "))
    iterations = int(input("Enter maximum iterations: "))
    position, value = hill_climbing(start, step, iterations)
    print("Best position =", position)
    print("Maximum value =", value)
