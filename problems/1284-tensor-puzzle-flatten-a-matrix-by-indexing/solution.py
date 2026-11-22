import numpy as np

def flatten(A: np.ndarray) -> np.ndarray:
    """Row-major flatten of 2-D array A without reshape/ravel."""
    m , n = A.shape
    t = np.arange(m*n)
    return A[t//n,t%n]
