
def auto_matrix(m,n):
    output_matrix = []
    for y in range(n):
        output_matrix_r = []
        for x in range(m):
            output_matrix_r.append(m * y + x + 1)
        output_matrix.append(output_matrix_r)
    return output_matrix

def writeMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print()

n, m = map(int, input().split())
matrix = auto_matrix(m, n)
writeMatrix(matrix)