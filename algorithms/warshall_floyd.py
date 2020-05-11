def warshall_floyd(d, V): #d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                
    return d
