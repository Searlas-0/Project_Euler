def main():
    greatest_prime = find_greatest_prime(60085147514383838495885855895)
    print(greatest_prime)

def find_greatest_prime(x):
    current_factor = x
    prime_factors = []
    prime_numbers = [2]
    while True:
        y , p = find_factor(current_factor, prime_numbers)
        if not y:
            prime_numbers = find_next_prime(prime_numbers)
            continue 
        prime_factors.append(p)
        print(prime_factors)
        if is_prime(y):
            prime_factors.append(y)
            print(prime_factors)
            return y
        current_factor = y

def find_next_prime(prime_numbers):
    start = prime_numbers[-1]
    trial = start + 1
    while True:
        if is_prime(trial):
            prime_numbers.append(trial)
            print(prime_numbers[-1])
            return prime_numbers
        trial += 1

def is_prime(x):
    n = 2
    while True:
        if n == x:
            return x 
        if x % n == 0:
            return False
        n += 1

def find_factor(y, prime_numbers):
    for prime in prime_numbers:
        if y % prime == 0:
            new_factor = y / prime
            return new_factor, prime
    return False, False

main()