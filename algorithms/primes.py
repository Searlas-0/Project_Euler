import numpy as np
import math

def sieve_of_eratosthenes(n):
    sieve = np.ones(n + 1, dtype=bool)
    primes = []
    sieve[0:2] = False
    for  i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = False
    for i in range(2,n + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def nth_prime(n):
    if n < 7:
        upper = 14
    else:
        upper = math.ceil(n * (math.log(n) + math.log(math.log(n))))

    primes = sieve_of_eratosthenes(upper)
    return primes[n-1]


    