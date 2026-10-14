import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
    x = np.array(x)
    s = np.exp(x - np.max(x))
    s = s / np.sum(s)
    J = np.diag(s) - np.outer(s, s)
    return J.tolist()