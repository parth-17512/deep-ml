import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    singular_values = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(singular_values > tol))