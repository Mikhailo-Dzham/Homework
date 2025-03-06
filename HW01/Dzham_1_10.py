import math

Sk1, R1 = map(float, input().split())
p = 3.14159265
R2 =  math.sqrt(((p * (R1**2)) - Sk1)/ p)

#R2 = round(R2, 2)

#R2 = "{:.2f}".format(R2)



print(f"{R2:0.2f}")