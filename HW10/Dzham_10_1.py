def matrix_input(sizey = 0):
    output_matrix = []
    for i in range(sizey):
        string_output_matrix = list(map(float, input().split()))
        output_matrix.append(string_output_matrix)
    return output_matrix

def proviryator_for_el_mtrx(mtrx):

    counter = 0
    sum_el = 0

    for y in range(len(mtrx)):
        for x in range(len(mtrx[0])):
            el = mtrx[y][x]

            if el < 0 and el % 2 == 0:
                counter +=1
                sum_el += el

    print(f"{counter}{sum_el:0.0f}")


#################### MAIN ################################
matrix_size = int(input())
matrix = matrix_input(matrix_size)
proviryator_for_el_mtrx(matrix)

