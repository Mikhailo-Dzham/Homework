def nsd_finder(a, b):
    while b:
        a, b = b, a % b
    return a

def nsk_finder(nsk, n):
    nsd = nsd_finder(nsk, n)
    nsk = (nsk * n) // nsd
    return nsk

#############################

limit = int(input())
multi_nsk = limit
for i in range(1, limit):
    if multi_nsk % (limit - i) ==0:
        continue
    else:
        multi_nsk = nsk_finder(multi_nsk, limit - i)

print(multi_nsk)
