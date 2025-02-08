import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.primes import nth_prime
import math

if __name__ == '__main__':
    n = int(input("Please choose an integer:"))
    print(nth_prime(n))
    
