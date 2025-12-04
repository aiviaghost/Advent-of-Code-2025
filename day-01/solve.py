import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = f.readlines()

MOD = 100


def solve_1():
    ans = 0
    dial = 50
    for line in data:
        dir, ticks = -1 if line[0] == "L" else 1, int(line[1:])
        dial = (dial + dir * ticks) % MOD
        ans += dial == 0
    print(ans)


def solve_2():
    ans = 0
    dial = 50
    for line in data:
        dir, ticks = -1 if line[0] == "L" else 1, int(line[1:])
        for _ in range(ticks):
            dial = (dial + dir) % MOD
            ans += dial == 0
    print(ans)


solve_1()
solve_2()
