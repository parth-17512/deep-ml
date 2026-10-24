
import numpy as np

def check_positive_definite(matrix: list) -> dict:
    A = np.array(matrix, dtype=float)

    # Validate square matrix
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

    # Calculate sorted eigenvalues
    eigenvalues = np.linalg.eigvalsh(A) if np.allclose(A, A.T) else np.linalg.eigvals(A)

    # Check symmetry and positive eigenvalues
    is_positive_definite = (
        np.allclose(A, A.T)
        and np.all(eigenvalues > 1e-10)
    )

    return {
        "is_positive_definite": bool(is_positive_definite),
        "eigenvalues": [round(float(x), 4) for x in sorted(eigenvalues)]
    }
