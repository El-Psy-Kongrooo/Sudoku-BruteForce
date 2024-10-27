import copy
import time
import sys

default_board = [
     ".........",
     "5.3.67...",
     "9..3421..",
     ".....4...",
     "..1...72.",
     "..2.1....",
     ".3......9",
     ".8.1..2..",
     "...75.8.6"
 ]

def main():
    global board
    if len(sys.argv) > 1:
        board = sys.argv[1:10]
        if not validate_board(board):
            print("Invalid board: Each row must have 9 characters, and only digits 1-9 or '.' are allowed.")
            return
    else:
        board = default_board
    for idx, line in enumerate(board):
        board[idx] = list(line)

    solve()
    printBoard()

def validate_board(board):
    if len(board) != 9:
        return False
    for row in board:
        if len(row) != 9: 
            return False
        for char in row:
            if char not in "123456789.": 
                return False

    return True
    
       
def solve():
    global board
    
    try:
        fillAllObvious()
    except:
        return False
    
    if isComplete():
        return True
    
    i,j = 0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == ".":
                i,j = rowIdx, colIdx
                
    possibilities = getPossibilities(i,j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
    
        board[i][j] = value
        printBoard()
        result = solve()
        if result == True:
            return True
        else:
            board = copy.deepcopy(snapshot)
            
    return False

def fillAllObvious():
    global board
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities(i,j)
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    printBoard()
                    somethingChanged = True             
        if somethingChanged == False:
            return
                
def getPossibilities(i,j):
    global board
    if board[i][j] != ".":
        return False
        
    possibilities = {str(n) for n in range(1,10)}
    
    for val in board[i]:
        possibilities -= set(val)
        
    for idx in range(0,9):
        possibilities -= set( board[idx][j] )
        
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
    
    subboard = board[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]
    
    for row in subboard:
        for col in row:
            possibilities -= set(col)
            
    return list(possibilities)

def printBoard():
    global board
    colcount = 1
    rowcount = 1
    for row in board:
        for col in row:
            print(col, end=" ")
            if colcount == 3:
                print("|", end=" ")
                colcount = 0
            colcount = colcount + 1 
        print("")
        if rowcount == 3:
            print("-----------------------")
            rowcount = 0
        rowcount = rowcount + 1 
    print("")
    time.sleep(0.5)

        
def isComplete():
    for row in board:
        for col in row:
            if (col == "."):
                return False
                
    return True
    
main()