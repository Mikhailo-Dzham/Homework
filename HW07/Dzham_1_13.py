list =[]

def dif(x):
    my_string = str(x)
    char_count = {}
    duplicates = []

    for char in my_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return [char for char, count in char_count.items() if count > 1]

def run(x ,y):
    for i in range(int(x),int(y)+1):
        if len(dif(i)) == 0:
            list.append(str(i))



n = input().split(" ")

run(n[0],n[1])

print(' '.join(list))