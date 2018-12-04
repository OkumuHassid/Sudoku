
import random

class SudokuBackEnd2:

    def gen_random_no:
        s = random.randint(1, 9)
        return s

    def gen_random_row:
        s = random.randint(0, 8)
        return s

    def gen_random_col:
        s = random.randint(0, 8)
        return s