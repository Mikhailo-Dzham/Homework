from rational import Rational

m = Rational(12.5)
n = Rational(2)
# print(m.n, m.d)
# print(m1.n, m1.d)
# k = m1 * 3
# print(k.n, k.d)
# print(m())
# print(m["n"])
# x = 4  -  92  -  79  *  59  *  Rational ("90/16")  *  75  -  55  *  Rational("82/41")  *  19
# print(x["n"], x["d"])
r = m + n
print(r.n, r.d)

# with open("input.txt", 'r') as f:
#     for line in f:
#         ln = line.split()
#         for e, i in enumerate(ln):
#             if "/" in i:
#                 ln[e] = f"Rational('{i}')"
#                 pass
#             # print(ln[e])
#         ln = " ".join(ln)
#         print(eval(ln))