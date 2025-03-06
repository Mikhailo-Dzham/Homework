#Спочатку введіть назву файла без '.txt'
#Потім оберіть варіант abcd відповідно до умови задачі
#Якщо ввести 'random' буде згенеровано файл 'file.txt' за заданими параметрами


import math
import random


def randomaizer(min_r, max_r, count):
    random_integers = [random.randint(min_r, max_r) for _ in range(count)]

    with open('file.txt', 'w') as random_f:
        print(*random_integers, file=random_f)


def variants(var):
    if var == 'a':
        evens_count(file)
    elif var == 'b':
        quadro_not_even_count(file)
    elif var == 'c':
        difference(file)
    elif var == 'd':
        max_sequense(file)


def evens_count(file):
    count = 0
    for el in file:
        if el % 2 == 0:
            count += 1
    print(count)


def quadro_not_even_count(file):
    count = 0
    for el in file:
        if el % 2 == 0 and el > 0:
            sqre_el = el ** 0.5
            if sqre_el == int(sqre_el):
                count += 1
    print(count)


def difference(file):
    max_ = -math.inf
    min_ = math.inf
    for el in file:
        if el > max_ and el % 2 == 0:
            max_ = el
        if el < min_ and el % 2 != 0:
            min_ = el
    print(max_ - min_)

def max_sequense(file):
    max_strike = 1
    strike = 1
    last = file[0]
    for el in file[1:]:
        if el > last:
            strike +=1
            if strike > max_strike:
                max_strike = strike
        else:
            strike = 1
        last = el
    print(max_strike)


##############################################

file_name = input()

if file_name == 'random':
    print("Введіть нижній ліміт, верхній ліміт, кількість рандомних чисел:")
    boot_lim, top_lim, count_random = map(int, input().split())
    randomaizer(boot_lim, top_lim, count_random)
    with open('file.txt', 'r') as f:
        file = list(map(int, f.read().split()))
else:
    try:
        file_name += '.txt'
        with open(file_name, 'r') as f:
            file = list(map(int, f.read().split()))
    except FileNotFoundError:
        print("Файл не знайдено")

print("Оберіть варіант завдання (abcd):")
var = input()
variants(var)
