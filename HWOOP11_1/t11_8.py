def a_sum(n):
    n_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            n_sum -=1
    if n % 2 != 0:
        n_sum += n
    return n_sum



print(a_sum(11))

