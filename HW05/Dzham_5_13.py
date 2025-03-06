n = int(input())

lst = map(float, input().split())

suma = 0
count = 0
for num in lst:
    if num <= 0:
        continue
    else:
        suma += num
        count +=1
if count == 0:
    print("Not Found")
else:
    print(f"{(suma / count):0.2f}")