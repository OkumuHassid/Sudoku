
import random

class SudokuBackEnd:

    def gen_random_no(self):
        s = random.randint(1, 9)
        return s

    def check_row(self, SudokuArray, col, number):
        for i in range(9):
            if SudokuArray[i][col] == number:
                return False
        return True

    def check_col(self, SudokuArray, row, number):
        for i in range(9):
            if SudokuArray[row][i] == number:
                return False
        return True

    def check_cube(self, SudokuArray, row, col, number):
        if row <= 2 and col <= 2:
            for i in range(3):
                for j in range(3):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 2 and col <= 5:
            for i in range(3):
                for j in range(3, 6):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 2 and col <= 8:
            for i in range(3):
                for j in range(6, 9):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 5 and col <= 2:
            for i in range(3, 6):
                for j in range(3):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 5 and col <= 5:
            for i in range(3, 6):
                for j in range(3, 6):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 5 and col <= 8:
            for i in range(3, 6):
                for j in range(6, 9):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 8 and col <= 2:
            for i in range(6, 9):
                for j in range(3):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 8 and col <= 5:
            for i in range(6, 9):
                for j in range(3, 6):
                    if SudokuArray[i][j] == number:
                        return False
            return True
        elif row <= 8 and col <= 8:
            for i in range(6, 9):
                for j in range(6, 9):
                    if SudokuArray[i][j] == number:
                        return False
            return True