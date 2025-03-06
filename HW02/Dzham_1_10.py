n = abs(int(input()))
first = n // 100
last = n % 10
if first > last:
    print(first)
elif last > first:
    print(last)
else:print("=")