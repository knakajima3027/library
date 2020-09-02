# d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
# 計算量: O(n^3)
def warshall_floyd(d: list, V: int) -> list: 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                
    return d