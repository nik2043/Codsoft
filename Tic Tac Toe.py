import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(len(board)):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board)-1-i] == player for i in range(len(board))):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        if is_board_full(board) or check_winner(board, human) or check_winner(board, ai):
            break

        if _ % 2 == 0:
            print("Human's turn (X):")
            while True:
                row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = human
                    break
                else:
                    print("Cell already occupied. Try again.")
        else:
            print("AI's turn (O):")
            move = best_move(board)
            board[move[0]][move[1]] = ai

        print_board(board)

    if check_winner(board, human):
        print("Human wins!")
    elif check_winner(board, ai):
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
