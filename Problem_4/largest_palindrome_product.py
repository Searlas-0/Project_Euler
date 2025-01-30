
def largest_palindrome_product(x):
    pali_list = create_palindromes(x)
    while True:
        for pali in pali_list:
            factors = factors_exists(pali, x)
            if factors:
                print(pali, factors)
                return pali, factors
        return 

def create_palindromes(half_size):
    pali = []
    start = half_size * '9'
    current = start
    end = int('1' + '0' * (half_size - 1))
    while int(current) >= end: 
        n = ''
        for i in current:
            n = i + n
        palindrome = int(current + n)
        pali.append(palindrome)
        current = str(int(current) - 1)
    return pali

def factors_exists(pali, half_size):
    start = int(half_size * '9')
    n = start
    end = int('1' + '0' * (half_size - 1))
    while n >= end:
        if pali % n == 0:
            n2 = int(pali/n)
            if n2 < start:
                return [n , n2]
        n -= 1
    return False 


largest_palindrome_product(3)