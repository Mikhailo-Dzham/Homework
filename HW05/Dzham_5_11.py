n = int(input())
lst = list(map(int, input().split()))
lst = lst[-1:] + lst[:-1]
print(*lst)