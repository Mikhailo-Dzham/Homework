incom_str = input()
abetka = "abcdefghijklmnopqrstuvwxyz"
output_str = []
for char in incom_str:
    if char in abetka:
        output_str.append(char)
output_str = sorted(output_str)
print("".join(output_str))
