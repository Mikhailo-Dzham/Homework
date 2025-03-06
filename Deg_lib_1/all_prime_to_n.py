def all_prime_to_(limit):

    prime_pack = [True] * (limit + 1)
    prime_pack[0] = prime_pack[1] = False

    for i in range(2, int(limit**0.5) +1):
       if prime_pack[i]:
           for j in range(i * i, limit + 1, i):
               prime_pack[j] = False

    return [num for num, is_prime in enumerate(prime_pack) if is_prime]

counter = 1
lim = 10 ** int(input())
primes = all_prime_to_(lim)
print(primes[-1])
# for prime in primes:
#     counter +=1
#     print(counter, prime)



