from sudoku import Sudoku
import time


def checkValidity(myBoard, row, col):
    if not checkRow(myBoard, row, col):
        return False
    if not checkCol(myBoard, row, col):
        return False
    if not checkSquare(myBoard, row, col):
        return False
    return True


def checkRow(myBoard, row, col):
    number = myBoard[row][col]
    for i in range(0, 9):
        if myBoard[row][i] == number and i != col:
            return False
    return True


def checkCol(myBoard, row, col):
    number = myBoard[row][col]
    for i in range(0, 9):
        if myBoard[i][col] == number and i != row:
            return False
    return True


def checkSquare(myBoard, row, col):
    number = myBoard[row][col]
    squarerow = row // 3
    squarecol = col // 3
    for i in range(squarerow*3, squarerow*3+3):
        for j in range(squarecol*3, squarecol*3+3):
            if myBoard[i][j] == number and not (row == i and col == j):
                return False
    return True


def complete(myBoard):
    for row in range(0, 9):
        for col in range(0, 9):
            if not myBoard:
                return False
            if not myBoard[row][col]:
                return False
    return True


def printSoduko(myBoard):
    for i in range(0, 9):
        print(myBoard[i])
        print("+-------+-------+-------+")


def solveSudoku(myBoard):
    if complete(myBoard):
        return myBoard

    for row in range(0, 9):
        for col in range(0, 9):
            if not myBoard[row][col]:
                for guess in range(1, 10):
                    myBoard[row][col] = guess
                    if checkValidity(myBoard, row, col):
                        solvedBoard = solveSudoku(myBoard)
                        if complete(solvedBoard):
                            return solvedBoard
                myBoard[row][col] = None
                return False
    return False


if __name__ == '__main__':
    counter = 0
    timerStart = time.perf_counter_ns()
    for _ in range(1, 1001):
        puzzle = Sudoku(3).difficulty(0.99)
        board = puzzle.board
        solution = solveSudoku(board)
    timerEnd = time.perf_counter_ns()
    print(f"Timer: {(timerEnd-timerStart) / 1000000000}s")
