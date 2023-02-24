gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], 
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
rows = 6
cols = 7

def placePiece(col, piece):
    if col <= 0 or col >= 8:
        raise Exception("Invalid placement!")
    if piece != "X" and piece != "O":
        raise Exception("Invalid piece!")
    row = 5 
    while gameBoard[row][col] != "":
        row = row - 1
        if row < 0:
            raise Exception("Column full!")
    gameBoard[row][col] = piece

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

