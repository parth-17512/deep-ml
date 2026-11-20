import numpy as np

def sequence_mask(values: np.ndarray, lengths: np.ndarray) -> np.ndarray:
    """Zero out positions j >= lengths[i] in each row i."""
    batch ,seq = values.shape
    rows = np.arange(seq).reshape(1,seq)
    cols = lengths.reshape(batch,1)
    mask = rows < cols
    return np.where(mask,values,0)
