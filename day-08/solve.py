import math
import re
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate, combinations, product

with open("input", "r") as f:
    data = list(map(str.strip, f.readlines()))


class UnionFind:
    def __init__(self, n):
        self.repr = list(range(n))
        self.sz = [1] * n
        self.roots = set(range(n))

    def find(self, a):
        if a != self.repr[a]:
            self.repr[a] = self.find(self.repr[a])
        return self.repr[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sz[b] > self.sz[a]:
            a, b = b, a
        self.roots.remove(b)
        self.repr[b] = a
        self.sz[a] += self.sz[b]

    def is_same_component(self, a, b):
        return self.find(a) == self.find(b)

    def get_component_sizes(self):
        return [self.sz[r] for r in self.roots]


def dist2(u, v):
    return sum((u[i] - v[i]) ** 2 for i in range(3))


def solve_1():
    nodes = [tuple(map(int, line.split(","))) for line in data]
    n = len(nodes)
    node_to_idx = dict(zip(nodes, range(n)))

    uf = UnionFind(n)
    edges = sorted((dist2(u, v), u, v) for u, v in combinations(nodes, 2))

    for _, u, v in edges[:1000]:
        if not uf.is_same_component(node_to_idx[u], node_to_idx[v]):
            uf.union(node_to_idx[u], node_to_idx[v])

    ans = math.prod(sorted(uf.get_component_sizes())[-3:])
    print(ans)


def solve_2():
    nodes = [tuple(map(int, line.split(","))) for line in data]
    n = len(nodes)
    node_to_idx = dict(zip(nodes, range(n)))

    uf = UnionFind(n)
    edges = sorted((dist2(u, v), u, v) for u, v in combinations(nodes, 2))

    for _, u, v in edges:
        if not uf.is_same_component(node_to_idx[u], node_to_idx[v]):
            uf.union(node_to_idx[u], node_to_idx[v])
            ans = u[0] * v[0]

    print(ans)


solve_1()
solve_2()
