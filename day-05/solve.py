import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


def solve_1():
    fresh = []
    it = iter(data)
    while line := next(it):
        a, b = map(int, line.split("-"))
        fresh.append((a, b))

    ans = 0
    for x in map(int, list(it)):
        for a, b in fresh:
            if a <= x <= b:
                ans += 1
                break
    print(ans)


def solve_2():
    fresh = []
    it = iter(data)
    while line := next(it):
        a, b = map(int, line.split("-"))
        fresh.append((a, b))
    fresh.sort()

    ans = 0
    prev_b = 0
    for a, b in fresh:
        if b <= prev_b:
            continue
        ans += b - max(a, prev_b + 1) + 1
        prev_b = b
    print(ans)


solve_1()
solve_2()
