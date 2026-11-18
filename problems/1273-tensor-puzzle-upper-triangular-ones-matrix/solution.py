import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    a = np.zeros((n,n))
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i <= j:
                a[i][j] +=1
    return a
