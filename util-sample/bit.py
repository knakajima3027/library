import itertools

#n桁のm値のbitを生成
def bit(n, m):
    bit_list = list(itertools.product([i for i in range(m)], repeat=n))
    return bit_list


# 自作版
def bit_list(x: int, n: int) -> list:
    '''
    xのn乗のbit配列を返す
    '''
    ans = []
    for i in range(x ** n):
        num = i
        j = 0
        table = [0 for _ in range(n)]
        while num:
            table[j] = num % x
            num = num // x
            j += 1

        ans.append(table)

    return ans
