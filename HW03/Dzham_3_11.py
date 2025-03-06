
n = int(input())
suma = 0
stak = 0
while n > 0:
    num = n % 10
    if num % 2 == 0:
        suma += num
        stak +=1

    n //=10
if stak == 0:
    suma = -1
print(suma)