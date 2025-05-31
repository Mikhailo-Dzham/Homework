def lambda_n(n):
    frac = 4 * n + 2
    for k in range(n, 0, -1):
        frac = 4 * k + 2 + 1 / frac
    return 2 + 1 / (6 + 1 / frac)
