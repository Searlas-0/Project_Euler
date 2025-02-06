import numpy as np

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
