import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """
    Compute an orthonormal basis for the null space (kernel) of matrix A.
    """

    # Perform full Singular Value Decomposition
    U, S, Vt = np.linalg.svd(A, full_matrices=True)

    # Determine the rank using the tolerance
    rank = np.sum(S > tol)

    # Extract right singular vectors corresponding to zero singular values
    null_space = Vt[rank:, :].T

    # Return the orthonormal basis
    return null_space