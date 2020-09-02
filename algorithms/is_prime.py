#　numが素数かどうかを判定
# 計算量: O(√n)
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False

    return num != 1


assert is_prime(2)) == True
assert is_prime(19) == True
assert is_prime(15135235) == True

