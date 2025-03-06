code = input()
key = int(input())
abetka = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
_decode = []
for char in code:
    if char in abetka:
        char_in_abetka = abetka.index(char)
        _decode.append(abetka[(char_in_abetka - key) % len(abetka)])
    else:
        _decode.append(char)

print("".join(_decode))