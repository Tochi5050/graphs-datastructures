class Solution:
    def __init__(self):
        self.rank = None
        self.edges_hash = {}
        self.vertices = None
        self.edges_hash_sorted = None
        self.count_edges = 0
        self.ans = 0

    def find(self, x):
        if x == self.vertices[x]:
            return x
        self.vertices[x] = self.find(self.vertices[x])
        return self.vertices[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.vertices[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.vertices[rootX] = rootY
            else:
                self.vertices[rootY] = rootX
                self.rank[rootX] += 1



    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        self.vertices = [i for i in range(len(points))]
        self.rank = [0] * len(points)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edge = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                self.edges_hash[(i, j)] = edge
                self.edges_hash_sorted = dict(sorted(self.edges_hash.items(), key=lambda item: item[1]))

        for (first, second), value in self.edges_hash_sorted.items():
            first_find = self.find(first)
            second_find = self.find(second)

            if self.count_edges == len(points) - 1:
                return self.ans

            if first_find != second_find:
                self.count_edges += 1
                self.union(first, second)
                self.ans += value







result = Solution()
points = [[3,12],[-2,5],[-4,1]]
print(result.minCostConnectPoints(points))