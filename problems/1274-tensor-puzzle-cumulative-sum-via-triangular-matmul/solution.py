import numpy as np

def cumsum(a: np.ndarray) -> np.ndarray:
    """Inclusive cumulative sum of 1-D array a without np.cumsum."""
    idx = np.arange(a.shape[0])
    mask = (idx[:,None] >= idx).astype(a.dtype)
    return mask @ a