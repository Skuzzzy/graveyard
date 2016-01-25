# https://projecteuler.net/problem=7
import math
primes = [2]
current_num = 3
while len(primes) < 10001:
    prime = True

    sqrt_current = math.sqrt(current_num)
    for num in primes:
        if num > sqrt_current:
            break
        if current_num % num == 0:
            prime = False
            break
    if prime:
        primes.append(current_num)
        print current_num

    current_num += 2


print primes[-1]


