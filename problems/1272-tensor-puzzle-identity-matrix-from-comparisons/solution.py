import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    a = np.zeros((n,n))
    for i in range(len(a)):
            a[i][i] += 1
    return a
