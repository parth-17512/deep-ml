import numpy as np

def rref(matrix):
    A = np.array(matrix, dtype=float)

    rows, cols = A.shape
    pivot_row = 0

    for col in range(cols):

        # Stop if all rows have been processed
        if pivot_row >= rows:
            break

        # Find the row with the largest absolute value in this column
        max_row = pivot_row + np.argmax(np.abs(A[pivot_row:, col]))

        # Skip the column if the pivot is approximately zero
        if np.isclose(A[max_row, col], 0):
            continue

        # Swap rows to bring the pivot into position
        A[[pivot_row, max_row]] = A[[max_row, pivot_row]]

        # Make the pivot equal to 1
        A[pivot_row] = A[pivot_row] / A[pivot_row, col]

        # Make all other entries in the pivot column zero
        for row in range(rows):
            if row != pivot_row:
                A[row] = A[row] - A[row, col] * A[pivot_row]

        pivot_row += 1

    # Remove small floating-point errors
    A[np.isclose(A, 0)] = 0

    return A