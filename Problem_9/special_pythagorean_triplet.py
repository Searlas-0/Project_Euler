import numpy as np

def special_triplet(n):
    arr = np.arange(1, n)

    for i in range(1,n):
        for j in range(1, n):
            if i == j:
                continue
            r = n - i - j
            if r == 0:
                continue
            trip = [r, i, j]
            n1 = (i**2 + j**2)**0.5
            n2 = (r**2 + j**2)**0.5
            n3 = (r**2 + i**2)**0.5
            if n1 in trip or n2 in trip or n3 in trip:
                print(i, j, r)
                return int(i*j*r)
 

print(special_triplet(1000))