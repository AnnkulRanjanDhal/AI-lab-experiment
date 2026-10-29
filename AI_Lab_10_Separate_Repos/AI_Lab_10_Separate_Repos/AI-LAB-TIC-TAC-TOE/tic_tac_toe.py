def print_board(board):
    for row in board:
        print(" | ".join(cell if cell != " " else " " for cell in row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return (all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3)))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    turns = 0
    while turns < 9:
        print_board(board)
        print(f"Player {player}'s turn")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Enter numeric row and column values.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position.")
            continue
        if board[row][col] != " ":
            print("Position already occupied.")
            continue
        board[row][col] = player
        turns += 1
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
