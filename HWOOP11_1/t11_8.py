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
    pass


for i in a_sum(10):
    print(i)
for i in range(1, 11):
    print(a_sum_bl(i))
