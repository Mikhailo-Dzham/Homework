import math

a, b, c = map(int, input().split())
D = b**2 - 4 * a * c

if  D < 0:
    print("No Roots")
elif D == 0:
    result1 = (-b) / (2 * a)
    print(f"One root: {result1:.0f}")
else:
    d = math.sqrt(D)
    result2 = (-b + d) / (2 * a)
    result1 = (-b - d) / (2 * a)
    if result2 > result1:
        print(f"Two Roots: {result1:.0f} {result2:.0f}")
    else:
        print(f"Two Roots: {result2:.0f} {result1:.0f}")







