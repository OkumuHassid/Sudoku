import time
from SudokuBackEnd import SudokuBackEnd

SudokuArray =    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 ]

array = SudokuBackEnd()


def through_col(row):
    col = 0
    while col < 9:

        state_col = False
        state_row = False
        state_cube = False
        timeout = time.time() + 10


        while not state_row or not state_cube or not state_col:
            while time.time() < timeout:
                number = array.gen_random_no()
                state_row = array.check_row(SudokuArray, col, number)
                state_col = array.check_col(SudokuArray, row, number)
                state_cube = array.check_cube(SudokuArray, row, col, number)
        SudokuArray[row][col] = number
        col += 1



def main():
    row = 0
    while row < 9:
        through_col(row)
        print(SudokuArray)
        row += 1


main()





