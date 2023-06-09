import time
from itertools import product

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Время выполнения функции {func.__name__}: {end_time} секунд.")
        return result
    return wrapper


def exact_cover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y


def solve(X, Y, solution):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()


def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols


def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

def sudoku_solver(grid):
    X = ([("rc", rc) for rc in product(range(9), range(9))] +
         [("rn", rn) for rn in product(range(9), range(1, 10))] +
         [("cn", cn) for cn in product(range(9), range(1, 10))] +
         [("bn", bn) for bn in product(range(9), range(1, 10))])
    Y = dict()
    for r, c, n in product(range(9), range(9), range(1, 10)):
        b = (r // 3) * 3 + c // 3
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))
        ]
    X, Y = exact_cover(X, Y)
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid
        break



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

@timer
def solve_sudoku(puzzle):
    sudoku_solver(puzzle)


for puzzle in puzzles:
    solve_sudoku(puzzle)