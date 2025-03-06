


def inversor(n):
    revers = 0
    while n:
        num = n % 10
        revers = revers * 10 + num
        n //=10
    return revers

def all_prime_to_(limit = 10**6):

    prime_pack = [True] * (limit + 1)
    prime_pack[0] = prime_pack[1] = False

    for i in range(2, int(limit**0.5) +1):
       if prime_pack[i]:
           for j in range(i * i, limit + 1, i):
               prime_pack[j] = False

    return [num for num, is_prime in enumerate(prime_pack) if is_prime]

n = int(input())
counter = 0
primes = all_prime_to_()
primes_set = set(primes)

for prime in primes:
    revers_ = inversor(prime)
    if prime != revers_ and revers_ in primes_set:
        counter +=1
        if counter == n:
            print(prime)
            break
if counter < n:
    print(-1)


