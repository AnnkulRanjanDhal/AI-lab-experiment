def minimax(depth, node_index, maximizing, scores, height):
    if depth == height:
        return scores[node_index]
    left = minimax(depth + 1, node_index * 2, not maximizing, scores, height)
    right = minimax(depth + 1, node_index * 2 + 1, not maximizing, scores, height)
    return max(left, right) if maximizing else min(left, right)

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 69, 5, 23, 63]
    height = 3
    print("The optimal value is:", minimax(0, 0, True, scores, height))
