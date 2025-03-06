n = int(input())

level = 0
alter = 0
n1 = n

while n1 > 0:
    num = n1 % 10
    alter = (alter * 10) + num
    n1 //= 10

while n != alter:
    n +=alter
    n2 = n
    alter = 0
    while n2 > 0:
        num = n2 % 10

        alter = (alter * 10) + num
        n2 //= 10
    level +=1


print(level)