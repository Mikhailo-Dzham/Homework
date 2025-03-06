n = int(input())
num = 1
for aboba in range(n):
    print(num, end=" ")
    num +=1
    while (num %2 == 0) or (num %3 == 0) or (num %5 == 0):
        num +=1




#for i in range(n):
   # print(i, end=" ")