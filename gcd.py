#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
