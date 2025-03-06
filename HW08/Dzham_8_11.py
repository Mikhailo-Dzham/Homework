import sys

sys.setrecursionlimit(10000000)

def aboba(a):
    if a % 10:
        return a % 10
    else:
        return aboba(a // 10)


def ameba(count, lim, result):
    if count > lim:
        print(result)
    else:
        return ameba(count + 1, lim, result + aboba(count))

def pytka():
    p, q = map(int, input().split())
    if p > 0 and q > 0:
        ameba(p, q, 0)
        pytka()

pytka()