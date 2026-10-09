
import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix using Gaussian elimination.

    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero

    Returns:
        The rank of the matrix (integer)
    """
    A = A.astype(float).copy()
    m, n = A.shape
    rank = 0

    for col in range(n):
        if rank >= m:
            break

        # Find the row with the largest absolute value in this column
        pivot_row = rank + np.argmax(np.abs(A[rank:, col]))

        # Skip this column if the largest value is approximately zero
        if abs(A[pivot_row, col]) <= tol:
            continue

        # Swap the pivot row with the current rank row
        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Eliminate values below the pivot
        for row in range(rank + 1, m):
            factor = A[row, col] / A[rank, col]
            A[row, col:] -= factor * A[rank, col:]

        # Count this pivot as one independent row
        rank += 1

    return rank
