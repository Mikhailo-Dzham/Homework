#ax**2+bx+c=0
def x_fsnder(d):
    global a, b
    return (b + d)/2*a

a, b, c = map(int, input().split())
assert a!=0, "То не квадратне рівняння"
D = b**2 - a*c*4
assert D>=0, "У рівняння тільки комплексні розв'язки"
if D==0:
    print(x_fsnder(D))
else:
    print(x_fsnder(-(D**0.5)), " ", x_fsnder((D**0.5)))