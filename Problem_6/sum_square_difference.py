import sys
import os
import math
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def sum_square_diff(n):
    arr = np.arange(1, n+1)
    arr_sq = arr ** 2 
    arr_sq_sum = np.sum(arr_sq)
    arr_sum = np.sum(arr)
    arr_sum_sq = arr_sum ** 2 
    diff = arr_sum_sq - arr_sq_sum
    return diff

if __name__ == '__main__':
    n = int(input("Please choose an integer:"))
    print(sum_square_diff(n))
     