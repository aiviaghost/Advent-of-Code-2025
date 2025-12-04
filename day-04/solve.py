import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


def find_active(grid):
    n, m = len(grid), len(grid[0])
    active = {(i, j) for i in range(n) for j in range(m) if grid[i][j] == "@"}
    return active


def find_moveable(grid, active):
    n, m = len(grid), len(grid[0])
    res = set()
    for i, j in active:
        if grid[i][j] == "@":
            rolls = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k != 0 or l != 0:
                        if 0 <= i + k < n and 0 <= j + l < m:
                            rolls += grid[i + k][j + l] == "@"
            if rolls < 4:
                res.add((i, j))
    return res


def solve_1():
    active = find_active(data)
    print(len(find_moveable(data, active)))


def solve_2():
    ans = 0
    grid = [list(row) for row in data]
    active = find_active(grid)
    while res := find_moveable(grid, active):
        for i, j in res:
            grid[i][j] = "."
        ans += len(res)
        active -= res
    print(ans)


solve_1()
solve_2()
