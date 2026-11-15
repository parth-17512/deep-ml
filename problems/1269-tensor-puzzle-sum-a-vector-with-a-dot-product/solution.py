import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    arr = np.arange(np.size(a))*0+1.0
    ans = np.dot(a,arr)
    return ans