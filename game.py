gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
illegalCols = []
rows = 6
cols = 7

def placePiece(col, piece): 
    while col <= 0 or col >= 8:
        print("Invalid placement!")
        col = input("Pick a new column: ")
        col = int(col)
    if piece != "X" and piece != "O":
        raise Exception("Invalid piece!")
    row = 5
    col -= 1
    while gameBoard[row][int(col)] != "":
        row = row - 1
        if row < 0:
            print("Column full!")
            illegalCols.append(col)
            while illegalCols.count(col) != 0:
                col = int(input("Pick a new column: "))
                col -= 1
    gameBoard[row][int(col)] = piece

def isGameWon(piece):
    #horizontal check
    for row in range(rows):
        for col in range(cols-3):
            if (gameBoard[row][col] == piece and gameBoard[row][col+1] == piece and 
                gameBoard[row][col+2] == piece and gameBoard[row][col+3] == piece):
                return True
    #vertical check
    for row in range(rows-3):
        for col in range(cols):
            if (gameBoard[row][col] == piece and gameBoard[row+1][col] == piece and 
            gameBoard[row+2][col] == piece and gameBoard[row+3][col] == piece):
                return True
    #up diagonal check
    for row in range(0, 3):
        for col in range(3, 7):
            if (gameBoard[row][col] == piece and gameBoard[row+1][col-1] == piece and 
                gameBoard[row+2][col-2] == piece and gameBoard[row+3][col-3] == piece):
                return True
    #down diagonal check
    for row in range(0, 3):
        for col in range(0, 4):
            if (gameBoard[row][col] == piece and gameBoard[row+1][col+1] == piece and
                gameBoard[row+2][col+2] == piece and gameBoard[row+3][col+3] == piece):
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



#play game:
play = input("Play game? Y/N: ")
while (play == "Y"):
    printGameBoard()
    columnOne = input("Player one, pick a column to place your piece. ")
    placePiece(int(columnOne), "X")
    printGameBoard()
    if (isGameWon("X")):
        print("Player one wins!")
        gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
        play = input("Play again? ")
        continue
    columnTwo = input("Player two, pick a column to place your piece. ")
    placePiece(int(columnTwo), "O")
    printGameBoard()
    if (isGameWon("O")):
        print("Player two wins!")
        gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
        play = input("Play again? ")
        continue
print("Thanks for playing!")