def convertor(n, b = 2):
    if n == 0:
        return 0


    convert_num = ""
    while n:
        num = str(n % b)
        convert_num = "".join([num, convert_num])
        n //=b
    return convert_num

m, a = map(int, input().split())
result = convertor(m, a)
print(result)