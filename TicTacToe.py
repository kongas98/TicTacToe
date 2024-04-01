import random

#the board
def TicTacboard():
    print("+===+===+===+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+===+===+===+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+===+===+===+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+===+===+===+")

#define turn order
def Turn_Selection():
    character =int(input("Would you like to go first or second? Write '1' for first and '2' for second:"))

    while character > 2 or character < 1:
        character =int(input("Would you like to go first or second? Write '1' for first and '2' for second:"))
    if character == 1:
        Player_Selection()
    else:
        Opponent_Selection()

#player selection
def Player_Selection():
    pl = 1
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
            win(pl)
            break
        else:
            print("This cell is already taken. Please pick another one.")


#opponent selection        
def Opponent_Selection():
    pl = 2
    while True:
        randpick = random.randrange(1,10)
        # Calculate row and column index based on the pc's pick
        row = (randpick - 1) // 3
        col = (randpick - 1) % 3

        # Check if the selected cell is empty
        if board[row][col] == " ":
            board[row][col] = "O"
            TicTacboard()
            win(pl)
            break
    

def win(player):
    winner_symbol = None
    if check_winner(board, "X"):
        print("YOU WIN!")
        winner_symbol = "X"
    elif check_winner(board, "O"):
        print("YOU LOSE!")
        winner_symbol = "O"

    if winner_symbol:
        print("GAME OVER")
        TicTacboard()
        quit()
    else:
        TicTacboard()
        if player == 2:
            Player_Selection()
        else:
            Opponent_Selection()

def check_winner(board, symbol):
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True

        # Check diagonals
        if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
            return True

    return False





board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]
round = 1
#Main Programm
print ("===TIC TAC TOE===")
#Call the current board
TicTacboard()
#Call the below def to see who plays first
Turn_Selection()






