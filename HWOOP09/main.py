from rational import *

# m = Rational("-2/4")
# n = Rational(0)
# print(m.n, m.d)
# print(m1.n, m1.d)
# k = m1 * 3
# print(k.n, k.d)
# print(m())
# print(m["n"])
# x = 4  -  92  -  79  *  59  *  Rational ("90/16")  *  75  -  55  *  Rational("82/41")  *  19
# print(x["n"], x["d"])
# r = m + n
# print(str(r))

for l in range(1, 4):
    with open(f"input0{l}.txt", 'r') as f:
        for line in f:
            ln = RationalList(line.split())
            if len(ln) == 0:
                continue
            for e, i in enumerate(ln):
                print(ln[e])
            print("result", sum(ln, start=Rational(0)))


