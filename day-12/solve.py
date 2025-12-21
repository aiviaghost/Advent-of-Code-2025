import math
import re
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = map(str.strip, f.readlines())

shape_data = [
    (next(data), sum(next(data).count("#") for _ in range(3)), next(data))[1]
    for _ in range(6)
]

ans = 0
for line in data:
    wh, *reqs = line.replace(":", "").split()
    w, h = map(int, wh.split("x"))
    reqs = list(map(int, reqs))

    if (w // 3) * (h // 3) >= sum(reqs):
        ans += 1
        continue

    if sum(r * shape_data[i] for i, r in enumerate(reqs)) >= w * h:
        continue

    ans += 1

print(ans)
