#x,yの最大公約数 計算量: O(logn)
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


#a,bの最小公倍数
def lcm(a: int, b: int) -> int:
    return a * b // gcd (a, b)


assert lcm(6, 12) == 12
assert lcm(67719, 17214) == 388571622
