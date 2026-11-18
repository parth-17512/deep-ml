import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    idx = np.arange(n)
    return (idx[:,None]<=idx[None,:]).astype(float)
