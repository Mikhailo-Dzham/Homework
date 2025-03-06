def convertor(n, b=10):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convert_num = ""
    while n:
        remainder = n % b
        convert_num = digits[remainder] + convert_num
        n //= b
    return convert_num

def inversor2(string):
    return str(string)[::-1]

m = int(input())
aboba = []
for i in range(2, 37):
    num = convertor(m, i)
    mun = inversor2(num)
    if num == mun:
        aboba.append(i)
if not aboba:
    print("none")
elif len(aboba) == 1:
    print("unique")
    print(*aboba)
else:
    print("multiple")
    print(*aboba)

