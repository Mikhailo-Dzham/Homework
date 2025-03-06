while True:
    result = 0
    p, q = map(int, input().split())
    if p < 0 and q < 0:
        break
    for i in range(p, q + 1):

        while not i % 10:
            i //=10
        else:
            result += i % 10
    print(result)
