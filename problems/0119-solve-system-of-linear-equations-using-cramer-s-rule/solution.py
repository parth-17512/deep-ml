import numpy as np

def cramers_rule(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.shape[0] != A.shape[1]:
        return -1

    A_det = np.linalg.det(A)

    if np.isclose(A_det, 0):
        return -1

    result = []

    for i in range(len(A)):
        x = A.copy()
        x[:, i] = b

        x1 = np.linalg.det(x)
        result.append(x1 / A_det)

    return result