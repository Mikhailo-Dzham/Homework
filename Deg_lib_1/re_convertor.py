def re_convertor(n, b = 10):
    step = 0
    convert_n = 0
    while n:
        convert_n += (n % 10) * b**step
        n //=10
        step +=1
    return convert_n

def convert_to_decimal(num_str, b=10):
    digits = {str(i): i for i in range(10)}
    for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        digits[c] = i + 10

    decimal = 0
    power = 0

    for digit in num_str[::-1]:
        decimal += digits[digit] * (b ** power)
        power += 1

    return decimal


m, a = map(int, input().split())
result = re_convertor(m, a)
print(result)

