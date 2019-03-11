#union-find木

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ
        self.num = [1 for _ in range(n)] #要素数

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.num[y] += self.num[x]
            self.num[x] = 0
        else:
            self.par[y] = x
            self.num[x] += self.num[y]
            self.num[y] = 0
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    #xが属する集合に属する要素数を返す
    def number(self, x):
        x = self.find(x)
        return self.num[x]
