def nsd_finder(a, b):
    while b:
        a, b = b, a % b
    return a

def nsk_finder(nsk, n):
    nsd = nsd_finder(nsk, n)
    nsk = (nsk * n) // nsd
    return nsk

################################################################

nsd_const, nsk_const = map(int, input().split())

nsdnsk = nsd_const * nsk_const
counter = 0

for i in range(nsd_const, nsk_const + 1):
    if i % nsd_const == 0 and nsk_const % i == 0:
        x = nsdnsk // i
        if nsd_finder(i, x) == nsd_const and nsk_finder(i, x) == nsk_const:
            counter +=1
print(counter)