import math

def alpha_beta(depth, node_index, maximizing, values, alpha, beta, height):
    if depth == height:
        return values[node_index]

    if maximizing:
        best = -math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, False,
                               values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, True,
                               values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best

if __name__ == "__main__":
    values = list(map(int, input("Enter 8 leaf values separated by spaces: ").split()))
    if len(values) != 8:
        print("Please enter exactly 8 values.")
    else:
        print("Optimal value:", alpha_beta(0, 0, True, values, -math.inf, math.inf, 3))
