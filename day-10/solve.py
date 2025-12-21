import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

from scipy.optimize import linprog

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


def solve_1():
    ans = 0
    for line in data:
        target, *wiring, _ = line.split()

        target_bit_vec = sum((c == "#") << i for i, c in enumerate(target[1:-1]))
        bit_vecs = [
            sum(1 << i for i in map(int, wires[1:-1].split(","))) for wires in wiring
        ]

        num_bit_vecs = len(bit_vecs)
        best = int.from_bytes(b"a very big number", "big")  # :D
        for mask in range(1, 1 << num_bit_vecs):
            res = reduce(
                int.__xor__,
                [bit_vecs[i] for i in range(num_bit_vecs) if (mask >> i) & 1],
            )
            if res == target_bit_vec:
                best = min(best, mask.bit_count())
        ans += best

    print(ans)


def solve_2():
    ans = 0
    for line in data:
        _, *wiring, target = line.split()

        buttons = [list(map(int, wires[1:-1].split(","))) for wires in wiring]
        target = list(map(int, target[1:-1].split(",")))

        c = [1] * len(wiring)
        A_eq = [[0] * len(wiring) for _ in range(len(target))]
        for i, button in enumerate(buttons):
            for j in button:
                A_eq[j][i] = 1

        options = {"presolve": False}  # one case fails otherwise
        sol = linprog(c, A_eq=A_eq, b_eq=target, integrality=1, options=options)
        ans += round(sol.fun)

    print(ans)


solve_1()
solve_2()
