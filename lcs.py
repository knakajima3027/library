def lcs(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                
            else:
                c[i][j] = c[i][j-1]
        
    return c[m][n]
