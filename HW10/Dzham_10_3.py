def matrix_input(sizey = 0):
    output_matrix = []
    for y in range(sizey):
        output_matrix_r = []

        for _ in range(sizey - y -1):
            output_matrix_r.append(2)
        output_matrix_r.append(0)
        for _ in range(sizey - len(output_matrix_r)):
            output_matrix_r.append(1)
        output_matrix.append(output_matrix_r)

    return output_matrix

def writeMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end="")
        print()

#############################################################

n = int(input())
matrix = matrix_input(n)
writeMatrix(matrix)