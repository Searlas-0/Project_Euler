def smallest_multiple(x):
    divisors = [i for i in range(x,0,-1)]
    removed = []
    f = []
    total = 1
    for n in divisors:
        temp = []
        factors = find_factors(n)
        for numb in factors:
            if numb not in f:
                temp.append(numb)
                print(temp,'temp')
        f += temp
        print(f,'f')
    print(f)
    for i in f:
        total *= i
    print(total)
    return total


def find_factors(n):
    factors = []
    for i in range(2, int(n/2)):
        if n % i == 0:
            factors.append(i)
            d = int(n / i)
            factors.append(d)
    if factors == []:
        factors = [n]
    print(f'factors={factors}')
    return factors
            








smallest_multiple(20)