import math

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

################################################################################


mod = 10**8
while True:
    try:
        l, m = map(int, input().split())
        gcd_nm = math.gcd(l, m)
        #print(fibonacci(gcd_nm))
        num1 = 1
        num2 = 0
        for i in range(gcd_nm-1):
            num1, num2 = (num1 + num2), num1
        print(num1 % mod)
    except EOFError:
        break

#Як не дивно, але рекурсивна версія значно повільніша за звичайну. Справа у тому що рекурсивна справляється не прохоитиме
#вже тоді, коли нсд перевищить приблизно 40 або й менше. Так як в одному тесті може бути до 1000 таких пар навіть при менших
# нсд сумарний час витрачений на пошук усіх цих значень буде дуже великим

