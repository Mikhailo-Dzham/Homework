n = int(input())
count = 0
if n != 0:
    for num in range(10, 100):
        sum1 = 0
        sum2 = 0
        NUM = num * n
        num_clon = num
        while NUM != 0:
            if num_clon != 0:
                sum1 += num_clon % 10
                num_clon //=10
            else:
                sum2 += NUM % 10
                NUM //=10
        if sum1 == sum2:
            count +=1
print(count)


