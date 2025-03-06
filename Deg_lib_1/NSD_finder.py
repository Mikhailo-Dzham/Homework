def nsd_finder(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
result = nsd_finder(n, m)
print(result)
