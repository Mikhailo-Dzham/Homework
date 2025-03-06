def convertor_sx(n, formula):
    if n:

        if n % 13 == 10:
            formula = "A" + formula
        elif n % 13 == 11:
            formula = "B" + formula
        elif n % 13 == 12:
            formula = "C" + formula
        else:
            formula = str(n % 13) + formula
        return convertor_sx((n // 13), formula)
    else:
        print(formula)


N = int(input())
formula_global = ""
if N == 0:
    print(0)
else:
    convertor_sx(N, formula_global)
