def matrix_rider(n):
    matrix = []
    for _ in range(n):
        string = list(map(int, input().split()))
        matrix.append(string)
    return matrix

n = int(input())

input_matrix = matrix_rider(n)

r, c = map(int, input().split())

for i in range(r):
    for j in range(c):
        print(input_matrix[i][j], end=' ')
    print()