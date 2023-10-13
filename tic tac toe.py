#tic tac toe game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if is_winner(board, current_player):
                winner = current_player
                break
            elif is_board_full(board):
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()