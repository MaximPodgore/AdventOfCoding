'''
just iterate through edges until there is is only one connected component
and return x of the x coordinates of the last edge added
'''
import math


class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank = [1] * n
		self.components = n

	def find(self, u):
		if self.parent[u] != u:
			self.parent[u] = self.find(self.parent[u])
		return self.parent[u]

	def union(self, u, v):
		ru = self.find(u)
		rv = self.find(v)
		if ru == rv:
			return False
		if self.rank[ru] > self.rank[rv]:
			self.parent[rv] = ru
		elif self.rank[ru] < self.rank[rv]:
			self.parent[ru] = rv
		else:
			self.parent[rv] = ru
			self.rank[ru] += 1
		self.components -= 1
		return True


def main():
	with open('day8_input.txt') as f:
		raw = f.read()
	junctions = raw.strip().split('\n')
	coordinates_list = [tuple(map(int, j.strip().split(','))) for j in junctions]

	# Build all pair edges with Euclidean distance
	edges = []
	for i in range(len(coordinates_list)):
		x1, y1, z1 = coordinates_list[i]
		for j in range(i + 1, len(coordinates_list)):
			x2, y2, z2 = coordinates_list[j]
			dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
			edges.append((dist, i, j))

	edges.sort()

	uf = UnionFind(len(coordinates_list))

	last_edge = None
	for dist, u, v in edges:
		merged = uf.union(u, v)
		if merged:
			last_edge = (u, v)
			if uf.components == 1:
				break

	if last_edge is None:
		print("No edges merged; input may be empty.")
		return

	u, v = last_edge
	# Return/print the x-coordinates of the endpoints of the last added edge
	xu = coordinates_list[u][0]
	xv = coordinates_list[v][0]
	mul = xu * xv
	print(mul)


if __name__ == '__main__':
	main()
