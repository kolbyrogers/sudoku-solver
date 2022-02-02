def inputBoard():
    while True:
        boardInput = input("Enter the board you wish to solve: ")
        if len(boardInput) != 81:
            print("\nBoard must be 81 characters.\n")
            continue
        else:
            break
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    for row in range(9):
        for col in range(9):
            if boardInput[col + (row * 9)] == '.':
                pass
            else: board[row][col] = int(boardInput[col + (row * 9)])
    return board

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print ("| ", end="")
            if j == 8:
                print (board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

def valid(board, num, pos):
    # Row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Group
    groupX = pos[1] // 3
    groupY = pos[0] // 3
    for i in range(groupY*3, groupY*3 + 3):
        for j in range(groupX*3, groupX*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True

def solveBoard(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solveBoard(board):
                return True
            
            board[row][col] = 0
    return False

def main():
    board = inputBoard()
    print("\nSolving...")
    solveBoard(board)
    print("---------------------")
    printBoard(board)

main()