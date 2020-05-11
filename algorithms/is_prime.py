#引数nが素数かどうかを判定
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False

    return num != 1


if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(19))
    print(is_prime(20))
