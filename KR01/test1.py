import math



limit = int(input())
lcm = 1
for i in range(1, limit):
    lcm = lcm * i // math.gcd(lcm, i)

print(lcm)
