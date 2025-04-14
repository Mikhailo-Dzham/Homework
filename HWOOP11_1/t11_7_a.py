def a_task(x, k=-1):
    x_k = x
    n = 1
    yield x_k
    while n !=k:
        x_k *= x ** 2 / (2 * n * (2 * n + 1))
        n +=1
        yield x_k


def b_task(x, k=-1):
    x_k = -x
    n = 2
    yield x_k
    while n !=k:
        x_k *= -(x / n)
        n +=1
        yield x_k


def c_task(x, k=-1):
    x_k = 1
    n = 2
    yield x_k
    while n !=k:
        x_k *= -x
        for j in range(n ** 2 - 2 * n, n ** 2 - n + 1):
            if not j:
                continue
            x_k /= j
        n +=1
        yield x_k


def d_task(x, k=-1):
    x_k = 1
    n = 1
    while n !=k:
        x_k *= x / n
        yield x_k * (n + 1)


result = d_task(2, )
for x in result:
    print(x)
print(result)
