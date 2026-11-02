import numpy as np

def gauss_seidel(A, b, n, x_ini=None):

    # Step 1: Get number of variables
    m = len(A)

    # Step 2: Initialize solution vector
    if x_ini is None:
        x = np.zeros(m)
    else:
        x = np.array(x_ini, dtype=float)

    # Step 3: Repeat for n iterations
    for i in range(n):

        # Step 4: Visit each equation
        for j in range(m):

            total = 0

            # Step 5: Calculate summation
            for k in range(m):
                if k != j:
                    total += A[j, k] * x[k]

            # Step 6: Update current variable
            x[j] = (b[j] - total) / A[j, j]

    # Step 7: Return final solution
    return x