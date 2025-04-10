def a_task(x, k):
    x_k = x
    for i in range(1, k+1):
        x_k *= x **2 / (2 * i * (2 * i +1))
    return x_k




result = a_task(2, 2)
print(result)