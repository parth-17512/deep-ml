import numpy as np

def bincount(a: np.ndarray, n_bins: int) -> np.ndarray:
    """Count occurrences of 0..n_bins-1 in integer array a."""
    cols = a[:,None]
    rows = np.arange(n_bins).reshape(1,n_bins)
    mask = (cols == rows)
    return mask.sum(axis=0)