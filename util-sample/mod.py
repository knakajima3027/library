#m (= 10**9 + 7)で割った余りを求めろ系の問題対策
#割り算は特殊なのでメモ(m = 10**9 + 7の時のみ)
#割り算以外は、計算のたびにmで割った余りを出す

'''
 (a / b) % m について考える( a ÷ b mod m)
1. フェルマーの小定理より、mが素数のときbで割る代わりに、bのm-2乗をかける
2. 1で出た値をmで割った余りを出す
''' 


m = 10**9 + 7

def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def mod(a, b):
    return mul(a, pos(b, mod-2))
