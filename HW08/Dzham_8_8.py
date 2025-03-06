def convertor_sx(n, formula):
    if n:

        if n % 2 == 1 and n // 2 !=0:
            formula = "SX" + formula
        elif n % 2 == 0:
            formula = "S" + formula
        return convertor_sx((n // 2), formula)
    else:
        print(formula)


N = int(input())
formula_global = ""
convertor_sx(N, formula_global)
# 10111
#
