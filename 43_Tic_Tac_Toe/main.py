#region INIT

print("*" * 10, "Tic Tac Toe game", "*" * 10)
board = list(range(1, 82))  # Initialize a 9x9 board

#endregion

def draw_board(board):

    """<DOC

        Draws the Tic Tac Toe board.

            PARAMETERS:
                        -board (list): The current state of the Tic Tac Toe board.

    DOC?>"""
    
    #region CODE

    print("-" * 46)
    for i in range(9):
        for j in range(9):
            print("|", f"{board[i * 9 + j]:2}", end=" ")
        print("|")
        print("-" * 46)

    #endregion

def take_input(player_token):

    """<DOC

        Takes input from the player to place their token on the board.

            PARAMETERS:

                        -player_token (str): The token ('X' or 'O') of the current player.

    DOC?>"""
  
    #region CODE

    valid = False
    while not valid:
        player_answer = input("Where will we put " + player_token + "? ")

        try:
            player_answer = int(player_answer)
        except:
            print("Invalid input. Are you sure you entered the number?")
            continue

        if player_answer >= 1 and player_answer <= 81:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("This cell is already occupied!")
        else:
            print("Invalid entry. Please enter a number from 1 to 81.")
    
    #endregion

def check_win(board):

    """<DOC

        Checks if there is a winner on the Tic Tac Toe board.

            PARAMETERS: 
                        -board (list): The current state of the Tic Tac Toe board.

            RETURNS: str or False: The winning player's token ('X' or 'O') if there is a winner, False otherwise.
            
    DOC?>"""

    #region CODE    

    # Check rows, columns, and diagonals for 3 continuous characters
    for i in range(9):
        for j in range(7):  # Adjusted to check for 3 continuous characters in a row
            # Check rows
            if board[i * 9 + j] == board[i * 9 + j + 1] == board[i * 9 + j + 2]:
                return board[i * 9 + j]
            # Check columns
            if board[j * 9 + i] == board[(j + 1) * 9 + i] == board[(j + 2) * 9 + i]:
                return board[j * 9 + i]
    # Check diagonals
    for i in range(7):  # Adjusted to check for 3 continuous characters in diagonals
        for j in range(7):
            if board[i * 9 + j] == board[(i + 1) * 9 + j + 1] == board[(i + 2) * 9 + j + 2]:
                return board[i * 9 + j]
            if board[i * 9 + j + 2] == board[(i + 1) * 9 + j + 1] == board[(i + 2) * 9 + j]:
                return board[i * 9 + j + 2]

    return False

    #endregion

def main(board):

    """<DOC

        Main function to run the Tic Tac Toe game.

            PARAMETERS:

                        -board (list): The initial state of the Tic Tac Toe board.

    DOC?>"""

    #region CODE
    
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                draw_board(board)
                print(tmp, " is the winner!")
                win = True
                break
        if counter == 81:
            print("Draw!")
            break
            
    #endregion

#region MAIN

main(board)
input("Press Enter to exit!")

#endregion
