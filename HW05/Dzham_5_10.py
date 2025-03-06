count_n = int(input())
n_lst = input().split()
count_m = int(input())
m_lst = input().split()

originaly_n_char = []
count = 0

for char_n in n_lst:
    if char_n not in m_lst:
        originaly_n_char.append(char_n)
        count +=1


print(count)
print(*originaly_n_char)