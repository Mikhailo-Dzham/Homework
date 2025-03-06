lst = input()
counter = 0
for i in range(len(lst)):
    if lst[i] in "+-*/%" and lst[i] != lst[i-1]:
        counter +=1
print(counter)