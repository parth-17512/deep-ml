import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    arr = np.arange(n)
    arr = arr*0
    arr = arr+1.0
    return arr
