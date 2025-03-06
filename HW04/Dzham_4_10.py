
n = int(input())
result = 0
if n == 1:
    for a in range(1, 10):
        if a % 2 != 0:
            continue
        for b in range (10):
            if b % 2 != 0:
                continue
            for c in range(10):
                if c % 2 != 0:
                    continue
                else: result += (a * 10 + b) *10 + c
elif n == 2:
    for a in range(1, 10):
        for b in range(10):
            if a >= b:
                continue
            for c in range(10):
                if b >= c:
                    continue
                else:
                    result +=1
elif n == 3:
    for a in range(1, 10):
        if a % 2 == 0:
            continue
        for b in range (10):
            if b % 2 == 0:
                continue
            for c in range(10):
                if c % 2 == 0:
                    continue
                else: result += (a * 10 + b) *10 + c
elif n == 4:
    for a in range(1, 10):
        for b in range(10):
            if a <= b:
                continue
            for c in range(10):
                if b <= c:
                    continue
                else:
                    result +=1
elif n == 5:
    for a in range(100, 1000):
        if a == (a // 100) **3 + (( a // 10 ) % 10 ) ** 3 + ( a % 10) **3:
            result += a
elif n == 6:
    for a in range(1, 10):
        for b in range(10):
            if a == b:
                continue
            for c in range(10):
                if b == c or c == a:
                    continue
                else:
                    result += 1



print(result)