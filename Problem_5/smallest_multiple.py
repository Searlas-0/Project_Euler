import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.primes import sieve_of_eratosthenes as primes
import math

def smallest_multiple(n):
    p = primes(n) 
    lcm = 1
    for i in p:
        e = math.floor(math.log(n)/math.log(i))
        lcm *= i**e
    return lcm

if __name__ == '__main__':
    n = int(input("Please choose an integer:"))
    print(smallest_multiple(n))
     