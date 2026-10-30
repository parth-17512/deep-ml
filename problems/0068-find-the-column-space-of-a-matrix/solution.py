import numpy as np

def matrix_image(A):
    A = np.asarray(A, dtype=float)

    independent_columns = []
    current_rank = 0

    for j in range(A.shape[1]):

        # Add the current column to previously selected columns
        candidate = A[:, independent_columns + [j]]

        # Calculate the rank
        new_rank = np.linalg.matrix_rank(candidate, tol=1e-10)

        # Keep the column only if it increases the rank
        if new_rank > current_rank:
            independent_columns.append(j)
            current_rank = new_rank

    # Return independent columns from the original matrix
    return A[:, independent_columns]