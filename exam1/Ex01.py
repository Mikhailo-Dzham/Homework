# input_1.txt



def read_koef(file_name):
    try:
        koef_list = []
        with open(file_name, 'r') as f:
            for line in f:
                line_values = line.split()
                assert len(line_values) == 3, "Неправильна кількість коефіцієнтів"
                line_values = list(map(float, line.split()))
                koef_list.append(line_values)
        executor(koef_list)

    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    except ValueError:
        print("Неправельні коефіцієнти")
        return None
    except KeyError:
        print("Забагато значень в рядку")
        return None

def executor(koefs):
    for row in koefs:
        aboba(row)


def aboba(inf):
    global two_x, one_x, no_x
    a, b, c = inf
    assert a != 0, "То не квадратне рівняння"
    D = b ** 2 - a * c * 4

    if D == 0:
        one_x[inf] = x_fsnder(D, a, b)
    elif D > 0:
        result = str(x_fsnder(-(D ** 0.5), a, b), " ", x_fsnder((D ** 0.5), a, b))
        two_x.update(inf, result)
    else:
        no_x.update(inf, None)

def x_fsnder(d, a, b):
    return (b + d) / 2 * a



def writer(two, one, no):
    with open("output", 'w' ) as f:
        for key in two:
            print(key, two[key])
        for key in one:
            print(key, one[key])
        for key in no:
            print(key, no[key])


name = input()
read_koef(name)
two_x = {}
one_x = {}
no_x = {}
writer(two_x, one_x, no_x)
