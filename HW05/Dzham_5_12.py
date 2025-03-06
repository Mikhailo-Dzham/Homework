n = int(input())
a = list(map(int, input().split()))
seen = set()
new_a = []
for x in a:
    if x not in seen:
        seen.add(x)
        new_a.append(x)
print(*new_a)
