import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = f.readlines()


def solve(x, num_to_pick):
    n = len(x)
    dp = [0] * (n + 1)
    for _ in range(num_to_pick):
        new_dp = [0] * (n + 1)
        for i in range(1, len(x) + 1):
            new_dp[i] = max(new_dp[i - 1], int(str(dp[i - 1]) + x[i - 1]))
        dp = new_dp
    return dp[-1]


def solve_1():
    ans = sum(solve(x, 2) for x in data)
    print(ans)


def solve_2():
    ans = sum(solve(x, 12) for x in data)
    print(ans)


solve_1()
solve_2()
