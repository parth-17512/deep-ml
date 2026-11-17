import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here
    A = np.asarray(A,dtype=float)
    idx = np.arange(A.shape[0])
    return A[idx,idx]
   
