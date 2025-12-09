'''
Problem requires storing 3d distance / or some sort of data structure?

x merges between boxes

output: multiply the 3 largest clumps together

only way:
minimum spanning forest. Manually calculate distances between all points and then go down and then use union find to merge them together

'''

import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
                self.rank[rootU] += 1

            
# input = """
# 162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# """
with open('day8_input.txt') as f:
    input = f.read()
junctions = input.strip().split('\n')
coordinates_list = [tuple(map(int, junction.strip().split(','))) for junction in junctions]

edges = []
for i in range(len(coordinates_list)):
    x1, y1, z1 = coordinates_list[i]
    for j in range(i+1, len(coordinates_list)):
        x2, y2, z2 = coordinates_list[j]
        dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        edges.append((dist, i, j))


edges.sort()
uf = UnionFind(len(coordinates_list))


for k in range(1000):
    dist, u, v = edges[k]
    uf.union(u, v)


component_sizes = {}
for i in range(len(coordinates_list)):
    root = uf.find(i)
    component_sizes[root] = uf.size[root]

top_3_clumps = sorted(component_sizes.values(), reverse=True)[:3]
result = top_3_clumps[0] * top_3_clumps[1] * top_3_clumps[2]
print(top_3_clumps)
print(result)


