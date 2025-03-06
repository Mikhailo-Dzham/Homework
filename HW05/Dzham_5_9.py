i_min, i_max, j_min, j_max = map(int, input().split())

counter = 0
ij_lib =[]

if i_max < i_min:
    i_max, i_min = i_min, i_max
if j_max < j_min:
    j_max, j_min = j_min, j_max

for i in range(i_min, i_max + 1):
    for j in range(j_min, j_max + 1):
        ij = i * j
        if ij not in ij_lib:
            ij_lib.append(ij)
            counter +=1
        print(i, j,ij, counter)

print(counter)