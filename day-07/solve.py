import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


def find_S():
    return 0, data[0].index("S")


def solve_1():
    ans = 0
    vis = set()

    def dfs(r, c):
        nonlocal ans

        if (r, c) in vis:
            return
        vis.add((r, c))

        if r >= len(data) or c < 0 or c > len(data[0]):
            return

        if data[r][c] == "^":
            ans += 1
            dfs(r, c - 1)
            dfs(r, c + 1)
            return

        dfs(r + 1, c)

    dfs(*find_S())

    print(ans)


def solve_2():
    dp = {}

    def dfs(r, c):
        nonlocal dp

        if (r, c) in dp:
            return dp[r, c]

        if r >= len(data) or c < 0 or c > len(data[0]):
            return 1

        if data[r][c] == "^":
            dp[r, c] = dfs(r, c - 1) + dfs(r, c + 1)
            return dp[r, c]

        return dfs(r + 1, c)

    print(dfs(*find_S()))


solve_1()
solve_2()
