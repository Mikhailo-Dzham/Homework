def convert_to_decimal(number_str, base):
    decimal_value = 0
    for digit in number_str:
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        else:
            value = ord(digit) - ord('A') + 10
        decimal_value = decimal_value * base + value
    return decimal_value

def convert_from_decimal(number, base):
    if number == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while number > 0:
        result.append(digits[number % base])
        number //= base
    return ''.join(reversed(result))

def base_conversion(m, k, number_str):
    decimal_value = convert_to_decimal(number_str, m)
    return convert_from_decimal(decimal_value, k)


m, k = map(int, input().split())
number_str = input().strip()
print(base_conversion(m, k, number_str))