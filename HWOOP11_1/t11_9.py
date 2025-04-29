def a_p(k=-1):
    p = 0.75
    i = 2
    yield p
    while i != k:
        i += 1
        p *= 1 - 1 / i ** 2

