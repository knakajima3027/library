#x,yの最大公約数 計算量: O(logn)
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


assert gcd(6, 12) == 6
assert gcd(67719, 17214) == 3