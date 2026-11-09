# --- cell 1 ---
import numpy as np

def train(X, y, W, b):

    # Add a column of ones for bias
    X_bias = np.column_stack((X, np.ones(X.shape[0])))

    # Find optimal weights and bias
    params = np.linalg.lstsq(X_bias, y, rcond=None)[0]

    # Separate weights and bias
    W = params[:-1]
    b = params[-1]

    return W, b