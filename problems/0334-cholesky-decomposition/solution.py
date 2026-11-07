import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    Returns lower triangular matrix L or -1 if decomposition is impossible.
    """
    try:
        A = np.array(A, dtype=float)

        # Check for empty or invalid matrix
        if A.ndim != 2 or A.shape[0] == 0:
            return -1

        n, m = A.shape

        # Check if square
        if n != m:
            return -1

        # Check for symmetry
        if not np.allclose(A, A.T):
            return -1

        L = np.zeros((n, n))

        # Cholesky decomposition
        for i in range(n):
            for j in range(i + 1):

                sum_val = 0.0

                for k in range(j):
                    sum_val += L[i][k] * L[j][k]

                if i == j:
                    value = A[i][i] - sum_val

                    if value <= 0:
                        return -1

                    L[i][j] = np.sqrt(value)

                else:
                    L[i][j] = (A[i][j] - sum_val) / L[j][j]

        return L.tolist()

    except (ValueError, TypeError, IndexError):
        return -1