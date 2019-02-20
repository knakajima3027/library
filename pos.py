#xのn乗をmで割った余り

m = 10**9 + 7

def pos(x, n, m):
    res = 1
    while n > 0:
        if n%2 == 1:
            res = (res * x)%m
        x = (x * x)%m
        n = n // 2

    return res
