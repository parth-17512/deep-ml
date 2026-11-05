import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
    """
    Solve Ax = b using the Conjugate Gradient method.
    """

    # Step 1: Initialize solution
    x = np.zeros_like(b, dtype=float) if x0 is None else np.array(x0, dtype=float)

    # Step 2: Calculate initial residual
    r = b - A @ x

    # Step 3: Initial search direction
    p = r.copy()

    # Step 4: Initial residual squared
    rs_old = np.dot(r, r)

    # Step 5: Iterate
    for _ in range(n):

        # Calculate A multiplied by search direction
        Ap = A @ p

        # Calculate step size
        alpha = rs_old / np.dot(p, Ap)

        # Update solution
        x = x + alpha * p

        # Update residual
        r = r - alpha * Ap

        # Check convergence
        rs_new = np.dot(r, r)

        if np.sqrt(rs_new) < tol:
            break

        # Calculate direction adjustment
        beta = rs_new / rs_old

        # Update search direction
        p = r + beta * p

        rs_old = rs_new

    return x