import pprint
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Время выполнения функции {func.__name__}: {end_time} секунд.")
        return result
    return wrapper


@timer
def sudoku(puzzle):

    size = len(puzzle)

    if not all(len(row) == size for row in puzzle):
        return "Ошибка: поле не является квадратным"

    def empty(puzzle):
        for row in range(size):
            for column in range(size):
                if puzzle[row][column] == 0:
                    return (row, column)
        return None

    def validate_puzzle(value, position, puzzle):
        row, column = position
        for i in range(size):
            if value == puzzle[i][column] and i != row:
                return False
        for i in range(size):
            if value == puzzle[row][i] and i != column:
                return False
        subgrid_size = int(size ** 0.5)
        start_row = subgrid_size * (row // subgrid_size)
        start_column = subgrid_size * (column // subgrid_size)
        for i in range(subgrid_size):
            for j in range(subgrid_size):
                if value == puzzle[i+start_row][j+start_column] and (i+start_row != row or j+start_column != column):
                    return False
        return True

    def available_values(position, puzzle):
        row, column = position
        values = set(range(1, size + 1))
        values -= set(puzzle[row])
        values -= set(puzzle[i][column] for i in range(size))
        subgrid_size = int(size ** 0.5)
        subgrid_row = row // subgrid_size
        subgrid_column = column // subgrid_size
        values -= set(puzzle[i][j] for i in range(subgrid_size * subgrid_row, subgrid_size * (subgrid_row + 1))
                             for j in range(subgrid_size * subgrid_column, subgrid_size * (subgrid_column + 1)))
        return values


    def solve():
        current_position = empty(puzzle)

        if current_position is None:
            return True

        for value in available_values(current_position, puzzle):
            valid = validate_puzzle(value, current_position, puzzle)

            if valid:
                row, column = current_position
                puzzle[row][column] = value

                if solve():
                    return True

                puzzle[row][column] = 0

        return False

    solve()
    return puzzle


puzzles = [
    [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]],
    [[4,0,0,0,0,0,8,0,5],
     [0,3,0,0,0,0,0,0,0],
     [0,0,0,7,0,0,0,0,0],
     [0,2,0,0,0,0,0,6,0],
     [0,0,0,0,8,0,4,0,0],
     [0,0,0,0,1,0,0,0,0],
     [0,0,0,6,0,3,0,7,0],
     [5,0,0,2,0,0,0,0,0],
     [1,0,4,0,0,0,0,0,0]],
    ]


for puzzle in puzzles:
    pprint.pprint(sudoku(puzzle))
