import math


def a_p(k=-1):
    p = 0.75
    i = 2
    yield p
    while i != k:
        i += 1
        p *= 1 - 1 / i ** 2

def b_p(k=-1):
    p = 2 + 1 / math.factorial(1)
    i = 1
    yield p
    while i != k:
        i += 1
        p *= 2 + 1 / math.factorial(i)
        yield p

def c_p(k=-1):
    p = 2 / 3
    i = 1
    yield p
    while i != k:
        i += 1
        p *= (i + 1) / (i + 2)
        yield p





