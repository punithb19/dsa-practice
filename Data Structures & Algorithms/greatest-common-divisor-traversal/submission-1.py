class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        self.n -= 1
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

    def isConnected(self):
        return self.n == 1




class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_index = {}
        for i, n in enumerate(nums):
            f = 2
            while f*f <=n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n//f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i

        return uf.isConnected()
        