import random

# Define the initial state of the board
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]

# Display the Tic-Tac-Toe board
def TicTacboard(board):
    print("+===+===+===+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+===+===+===+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+===+===+===+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+===+===+===+")

# Define the function to determine the turn order
def Turn_Selection(board):
    character =int(input("Would you like to go first or second? Write '1' for first and '2' for second:"))

    while character > 2 or character < 1:
        character =int(input("Would you like to go first or second? Write '1' for first and '2' for second:"))
    if character == 1:
        Player_Selection(board)
    else:
        Opponent_Selection(board)

# Function for player's turn
def Player_Selection(board):
    while True:
        pick = int(input("What cell would you like to mark? (1-9): "))
        while pick < 1 or pick > 9:
            pick = int(input("What cell would you like to mark? (1-9): "))

        # Calculate row and column index based on the user's pick
        row = (pick - 1) // 3
        col = (pick - 1) % 3

        # Check if the selected cell is empty
        if board[row][col] == " ":
            board[row][col] = "X"
            TicTacboard(board)
            if check_winner(board, "X"):
                print("YOU WIN!")
                print("GAME OVER")
                Replay(board)
            elif is_tie(board):
                print("It's a tie!")
                print("GAME OVER")
                Replay(board)
            else:
                Opponent_Selection(board)
                break
        else:
            print("This cell is already taken. Please pick another one.")


# Function for opponent's turn       
def Opponent_Selection(board):
    while True:
        randpick = random.randrange(1,10)
        row = (randpick - 1) // 3
        col = (randpick - 1) % 3

        # Check if the selected cell is empty
        if board[row][col] == " ":
            board[row][col] = "O"
            TicTacboard(board)
            if check_winner(board, "O"):
                print("YOU LOSE!")
                print("GAME OVER")
                Replay(board)
            elif is_tie(board):
                print("It's a tie!")
                print("GAME OVER")
                Replay(board)
            else:
                Player_Selection(board)
                break
    
# Function to check for a tie
def is_tie(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to check winning conditions
def check_winner(board, symbol):
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True

        # Check diagonals
        if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
            return True

    return False

def Replay(board):
    replay_input = input("Would you like to play again?(Y/N): ")
    while replay_input.lower() != "y" and replay_input.lower() != "n":
        replay_input = input("Would you like to play again?(Y/N): ")
    if replay_input.lower() == "y":
        board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
            ]
        TicTacboard(board)
        Turn_Selection(board)
    else:
        quit()

# Main Program
print ("===TIC TAC TOE===")
# Display the initial board
TicTacboard(board)
# Determine the turn order
Turn_Selection(board)
