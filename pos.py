#aのb乗をmで割った余り

m = 10**9 + 7

def pos(a, b, m):
    if b == 0:
        return 1
    res = (a * a)**(b // 2)%m
    if b%2 == 1:
        res = (res * a)%m
    return res
