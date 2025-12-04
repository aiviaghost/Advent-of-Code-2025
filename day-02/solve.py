import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = f.readline()


def solve(pattern):
    ans = 0
    for r in data.split(","):
        a, b = map(int, r.split("-"))
        for x in range(a, b + 1):
            if re.fullmatch(pattern, str(x)):
                ans += x
    return ans


def solve_1():
    print(solve(r"(\d+)\1"))


def solve_2():
    print(solve(r"(\d+)\1+"))


solve_1()
solve_2()
