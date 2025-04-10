def a_task(x, k):
    x_k = x
    for i in range(1, k + 1):
        x_k *= x ** 2 / (2 * i * (2 * i + 1))
        yield x_k


def b_task(x, k):
    x_k = -x
    for i in range(2, k + 1):
        x_k *= -(x / i)
        yield x_k

def c_task(x, k):
    x_k = 1
    for i in range(2, k + 1):
        x_k *= -x
        for j in range(i**2-2*i, i**2-i+1):
            if not j:
                continue
            x_k /= j
        yield x_k

def d_task(x, k):
    x_k = 1
    for i in range(1, k+1):
        x_k *= x / i
        yield x_k * (i + 1)


result = d_task(2, 5)
for x in result:
    print(x)
print(result)
