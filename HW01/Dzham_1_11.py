import math

abcdf = input()
abcdf = map(float, abcdf.split())
a, b, c, d, f = abcdf

p1 = (a + b + f) /2
S1 = p1 * (p1-a) * (p1-b) * (p1-f)
S1 = math.sqrt(S1)

p2 = (c + d + f) /2
S2 = p2 * (p2-c) * (p2-d) * (p2-f)
S2 = math.sqrt(S2)

S3 = S2 + S1

print(S3)