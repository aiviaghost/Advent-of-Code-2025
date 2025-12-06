import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = f.readlines()


def solve_1():
    grid = [list(map(int, line.split())) for line in data[:-1]]
    ops = [int.__add__ if op == "+" else int.__mul__ for op in data[-1].split()]
    ans = 0
    num_cols = len(grid[0])
    for i in range(num_cols):
        nums = [row[i] for row in grid]
        ans += reduce(ops[i], nums)
    print(ans)


def transpose(grid):
    n, m = len(grid), len(grid[0])
    res = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][i] = grid[i][j]
    return res


def solve_2():
    grid = transpose(data[:-1])
    ops = (int.__add__ if op == "+" else int.__mul__ for op in data[-1].split())
    ans = 0
    seq = ["".join(filter(str.isdigit, row)) for row in grid]
    curr_idx = 0
    while 1:
        try:
            next_idx = seq.index("", curr_idx)
            nums = map(int, seq[curr_idx:next_idx])
            curr_idx = next_idx + 1
            ans += reduce(next(ops), nums)
        except:
            break
    print(ans)


solve_1()
solve_2()
