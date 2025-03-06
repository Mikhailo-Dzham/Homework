def inversor(n):
    revers = 0
    while n:
        num = n % 10
        revers = revers * 10 + num
        n //=10
    return revers

m = int(input())
result = inversor(m)
print(result)

def inversor2(string):
    return int(str(string)[::-1])