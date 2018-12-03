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


for row in range(9):
    for col in range(9):
        state_row = False
        state_col = False
        state_cube = False

        while not state_row or not state_col or not state_cube:
            number = array.gen_random_no()
            state_row = array.check_row(SudokuArray, col, number)
            state_col = array.check_col(SudokuArray, row, number)
            state_cube = array.check_cube(SudokuArray, row, col, number)

        SudokuArray[row][col] = number
    print(SudokuArray)
print(SudokuArray)