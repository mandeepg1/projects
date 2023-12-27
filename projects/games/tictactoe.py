# Tic Tac Toe Game by Mandeep Gujral
import random
def main():
    print("\nLet's Play Tic Tac Toe!\n")
    board = create_board()
    board_spacing = board_space(board)
    choosing, computer_choice = playerChoice()
    placing = boardPlacement(board, choosing)
    cpm = computer_move(board, computer_choice)
    
    while True:
        placing = boardPlacement(board, choosing)
        if is_game_over(board):
            break
        computer_move(board, computer_choice)

def create_board():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    return board

def board_space(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def playerChoice():
    while True:
        user_input = input("Pick X or O: ")
        if user_input.upper() == "X":
            computer_input = "O"
            print(f"You picked {user_input.upper()}!")
            print(f"The computer picked {computer_input}!")
            return user_input.upper(), computer_input
        elif user_input.upper() == "O":
            computer_input = "X"
            print(f"You picked {user_input.upper()}!")
            print(f"The computer picked {computer_input}!")
            return user_input.upper(), computer_input
        else:
            print("Invalid choice. Please pick X or O.")


def boardPlacement(board, user_letter):
    while True:
        userInput = input("Where do you want to place your letter? (Enter 1-9): ")
        if userInput.isdigit() and 1 <= int(userInput) <= 9:
            position = int(userInput) - 1
            row = position // 3
            col = position % 3
            if board[row][col] in ["X", "O"]:
                print("Oops! That position is already taken. Try again.")
            else:
                board[row][col] = user_letter
                board_space(board)
                break
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board, computer_choice):
    # Check for a winning move
    for i in range(9):
        row = i // 3
        col = i % 3
        if board[row][col] not in ["X", "O"]:
            # Simulate making the move
            board[row][col] = computer_choice
            if check_for_win(board, computer_choice):
                print("\nComputer makes a winning move:")
                board_space(board)
                return

            # Undo the move
            board[row][col] = str(i + 1)

    # Check for a blocking move (block the player from winning)
    for i in range(9):
        row = i // 3
        col = i % 3
        if board[row][col] not in ["X", "O"]:
            # Simulate the player's move
            board[row][col] = "X"
            if check_for_win(board, "X"):
                # Block the winning move
                board[row][col] = computer_choice
                print("\nComputer blocks the player:")
                board_space(board)
                return

            # Undo the move
            board[row][col] = str(i + 1)

    # If no winning or blocking move, make a random move
    available_positions = [i + 1 for i in range(9) if board[i // 3][i % 3] not in ["X", "O"]]
    if available_positions:
        position = random.choice(available_positions)
        row = (position - 1) // 3
        col = (position - 1) % 3
        board[row][col] = computer_choice
        print("\nComputer makes a move:")
        board_space(board)
    else:
        print("It's a draw!")


def is_game_over(board):
    # Check for a win
    if check_for_win(board, "X"):
        print("Player (X) wins!")
        print("Thanks for playing!!")
        return True
    elif check_for_win(board, "O"):
        print("Computer (O) wins!")
        return True

    # Check for a draw
    elif all(board[i // 3][i % 3] in ["X", "O"] for i in range(9)):
        print("It's a draw!")
        return True

    return False

def check_for_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

main()
