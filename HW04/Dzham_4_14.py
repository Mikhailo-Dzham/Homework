n = int(input())
sqrt = int(n ** (1/2))
test_d = 2
while test_d <= sqrt:
    if n % test_d == 0:
        break
    else:
        test_d +=1
        if test_d > sqrt:
            test_d = n
print(int(n / test_d))

