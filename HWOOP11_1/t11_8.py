def a_sum_bl(n):
    return -1 * (n // 2) + n * (n % 2)


def a_sum(k=-1):
    s = 1
    n = 1
    yield s
    while n != k:
        n += 1
        s += (-1) ** (n + 1) * n
        yield s

def b_sum(k=-1):
    s = 0.5
    n  = 2
    yield  s
    while n !=k:
        n +=1
        s += 1/((n-1)*n)
        yield s

def c_cum(k=-1):
    s = 0.5
    n = 2
    yield s
    while n !=k:
        n+=1
        s += (-1)**n * (n-1)/n
        yield s


try:
    for i in c_cum():
        last = i
except KeyboardInterrupt:
    print(last)
