def is_safe(board, row, col):
    for r in range(row):
        if board[r][col] == "Q":
            return False
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < len(board):
        if board[r][c] == "Q":
            return False
        r -= 1
        c += 1
    return True

def solve(board, row=0):
    if row == len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve(board, row + 1):
                return True
            board[row][col] = "."
    return False

if __name__ == "__main__":
    n = 8
    board = [["." for _ in range(n)] for _ in range(n)]
    if solve(board):
        print("One solution to the 8-Queens problem:")
        for row in board:
            print(" ".join(row))
    else:
        print("No solution found.")
