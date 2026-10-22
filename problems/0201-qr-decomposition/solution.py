import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    Q, R = np.linalg.qr(A)

    for i in range(min(Q.shape[1], R.shape[0])):
        if R[i, i] < 0:
            Q[:, i] *= -1
            R[i, :] *= -1

    return Q.tolist(), R.tolist()