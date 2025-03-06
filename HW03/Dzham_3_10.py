n = int(input())

nClon = n
result = 0
koef = 1
while nClon != 0:
    number = nClon % 10
    if number % 2 ==0:
        number +=1
    else:
        number -=1
    nClon //= 10

    result = result + number * koef
    koef *= 10
print(int(result))