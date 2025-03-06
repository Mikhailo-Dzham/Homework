n = int(input())
suma = 0
nsuma = abs(n)
while nsuma > 0:
    d = nsuma % 10
    suma += d
    nsuma //= 10
if (n % 2 == 0) ^ ((suma % 3 == 0) and (n < 0)):
    print("YES")
else: print("NO")
