import numpy as np

def low_rank_approximation(delta_W: np.ndarray, r: int) -> list:
    """
    Compute the best rank-r approximation of delta_W via truncated SVD.

    Args:
        delta_W: matrix of shape (m, n)
        r: target rank (1 <= r <= min(m, n))

    Returns:
        The rank-r approximation as a nested Python list of shape (m, n).
    """
    arr = np.asarray(delta_W, dtype=float)
    
    # Step 1: Compact SVD (U: (m, k), S: (k,), Vt: (k, n))
    U, S, Vt = np.linalg.svd(arr, full_matrices=False)
    
    # Step 2: Keep only the top r singular components
    U_r = U[:, :r]
    S_r = S[:r]
    Vt_r = Vt[:r, :]
    
    # Step 3: Reconstruct the rank-r matrix and return as nested Python lists
    approx = (U_r * S_r) @ Vt_r
    return approx.tolist()