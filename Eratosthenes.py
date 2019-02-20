#nまでの素数を列挙(エストラステネスの篩)
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i

    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
