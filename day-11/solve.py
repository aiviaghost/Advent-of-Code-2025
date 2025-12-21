import math
import re
from collections import Counter, defaultdict
from functools import cache, reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


adj = defaultdict(list)
for line in data:
    u, *vs = line.replace(":", "").split()
    adj[u] = vs


@cache
def dfs(curr):
    return sum(map(dfs, adj[curr]), curr == "out")


@cache
def dfs2(curr, target, exclude=None):
    return (
        1
        if curr == target
        else sum(
            dfs2(child, target, exclude) for child in adj[curr] if child != exclude
        )
    )


def solve_1():
    print(dfs("you"))


def solve_2():
    svr_to_dac = dfs2("svr", "dac", "fft")
    dac_to_fft = dfs2("dac", "fft")
    fft_to_out = dfs2("fft", "out", "dac")

    svr_to_fft = dfs2("svr", "fft", "dac")
    fft_to_dac = dfs2("fft", "dac")
    dac_to_out = dfs2("dac", "out", "fft")

    print(svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out)


solve_1()
solve_2()
