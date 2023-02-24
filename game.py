gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
rows = 6
cols = 7

def placePiece(col, piece): 
    if col <= 0 or col >= 8:
        print("Invalid placement!")
        #enter again
    if piece != "X" and piece != "O":
        print("Invalid piece!")
        #enter again
    row = 5 
    while gameBoard[row][col] != "":
        row = row - 1
        if row < 0:
            print("Column full!")
            #enter again
    gameBoard[row][col] = piece

def isGameWon(piece):
    #horizontal check
    for row in range(rows):
        for col in range(cols-3):
            if (gameBoard[row][col] == piece and gameBoard[row][col+1] == piece and 
                gameBoard[row][col+2] == piece and gameBoard[row][col+3] == piece):
                return True
    #vertical check
    for row in range(rows-2):
        for col in range(cols):
            if (gameBoard[row][col] == piece and gameBoard[row+1][col] == piece and 
            gameBoard[row+2][col] == piece and gameBoard[row+3][col] == piece):
                return True
    #diagonal check
    for row in range(rows-2):
        for col in range(cols-3):
            if (gameBoard[row][col] == piece and gameBoard[row+1][col+1] == piece and 
                gameBoard[row+2][col+2] == piece and gameBoard[row+3][col+3] == piece):
                return True
    #diagonal check
    for row in range(rows-2):
        for col in range(cols-3):
            if (gameBoard[row][col] == piece and gameBoard[row-1][col-1] == piece and
                gameBoard[row-2][col-2] == piece and gameBoard[row-3][col-3] == piece):
                return True
    return False

def printGameBoard():
    for j in range(cols):
        print("  " + str(j + 1) + " ", end="")
    print("")
    for i in range(rows):
        for j in range(cols):
            print("+---", end="")
        print("+")
        for j in range(cols):
            print("|   ", end="")
        print("|")
        for j in range(cols):
            if gameBoard[i][j] == "X":
                print("| X ", end="")
            elif gameBoard[i][j] == "O":
                print("| O ", end="")
            else:
                print("|   ", end="")
        print("|")
        for j in range(cols):
            print("|   ", end="")
        print("|")
    for j in range(cols):
            print("+---", end="")
    print("+")

printGameBoard()

def playGame():
    play = input("Play game? Y/N: ")
    while (play == "Y"):
        columnOne = input("Player one, pick a column to place your piece. ")
        placePiece(int(columnOne), "X")
        printGameBoard()
        if (isGameWon("X")):
            print("Player one wins!")
            play = input("Play again? ")
        columnTwo = input("Player two, pick a column to place your piece. ")
        placePiece(int(columnTwo), "O")
        printGameBoard()
        if (isGameWon("O")):
            print("Player two wins!")
            play = input("Play again? ")
    print("Thanks for playing!")

playGame()