x1, y1, x2, y2, koef = map(float, input().split())



x3 = (x1 + koef * x2) / (koef + 1)
y3 = (y1 + koef * y2) / (koef + 1)

# round(x3, 2)
# round(y3, 2)


print(f"{x3:0.2f}", f"{y3:0.2f}")