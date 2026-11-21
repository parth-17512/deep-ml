import numpy as np

def scatter_add(values: np.ndarray, indices: np.ndarray, n_bins: int) -> np.ndarray:
    values = np.asarray(values)
    indices = np.asarray(indices)
    
    # Build a 2-D one-hot indicator matrix of shape (n_bins, len(values))
    # Row k has True where indices == k, and False elsewhere
    mask = (np.arange(n_bins)[:, None] == indices[None, :])
    
    # Multiply by values and sum across the elements axis (axis=1)
    return (mask * values).sum(axis=1, dtype=values.dtype)