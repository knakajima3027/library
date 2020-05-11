import itertools

#n桁のm値のbitを生成
def bit(n, m):
    bit_list = list(itertools.product([i for i in range(m)], repeat=n))
    return bit_list
