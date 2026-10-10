import numpy as np

def gaussian_elimination(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)

    for i in range(n):
        p = i + np.argmax(np.abs(A[i:, i]))
        A[[i, p]] = A[[p, i]]
        b[[i, p]] = b[[p, i]]

        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] -= m * A[i, i:]
            b[j] -= m * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]

    return x.tolist()