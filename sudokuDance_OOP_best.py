from itertools import product
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


class ExactCover:
    def __init__(self, X, Y):
        self.X = {j: set() for j in X}
        for i, row in Y.items():
            for j in row:
                self.X[j].add(i)
        self.Y = Y

    def select(self, r):
        cols = []
        for j in self.Y[r]:
            for i in self.X[j]:
                for k in self.Y[i]:
                    if k != j:
                        self.X[k].remove(i)
            cols.append(self.X.pop(j))
        return cols

    def deselect(self, r, cols):
        for j in reversed(self.Y[r]):
            self.X[j] = cols.pop()
            for i in self.X[j]:
                for k in self.Y[i]:
                    if k != j:
                        self.X[k].add(i)

    def solve(self, solution):
        if not self.X:
            yield list(solution)
        else:
            c = min(self.X, key=lambda c: len(self.X[c]))
            for r in list(self.X[c]):
                solution.append(r)
                cols = self.select(r)
                for s in self.solve(solution):
                    yield s
                self.deselect(r, cols)
                solution.pop()


class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
        self.X = ([("rc", rc) for rc in product(range(9), range(9))] +
                  [("rn", rn) for rn in product(range(9), range(1, 10))] +
                  [("cn", cn) for cn in product(range(9), range(1, 10))] +
                  [("bn", bn) for bn in product(range(9), range(1, 10))])
        self.Y = dict()
        for r, c, n in product(range(9), range(9), range(1, 10)):
            b = (r // 3) * 3 + c // 3
            self.Y[(r, c, n)] = [
                ("rc", (r, c)),
                ("rn", (r, n)),
                ("cn", (c, n)),
                ("bn", (b, n))
            ]

    @timer
    def solve(self):
        exact_cover = ExactCover(self.X, self.Y)
        for i, row in enumerate(self.grid):
            for j, n in enumerate(row):
                if n:
                    exact_cover.select((i, j, n))
        for solution in exact_cover.solve([]):
            for (r, c, n) in solution:
                self.grid[r][c] = n
            yield self.grid
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


for puzzle in puzzles:
    solver = SudokuSolver(puzzle)
    solution = solver.solve()