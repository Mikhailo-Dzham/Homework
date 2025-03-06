# n = int(input())
# cubes = list(input())
# if n % 2 == 0:
#     print("OK")
# else:
count = int(input())
cubes = list(input())

if count % 2 == 0:
     print("Ok")
else:
    dict_ = {}
    for el in cubes:
        if el in dict_:
            dict_[el] += 1
        else:
            dict_[el] = 1

    for k in dict_:
        if dict_[k] % 2 !=0:
            print(k)
