# --- cell 1 ---
import numpy as np

def train(X, y, W, b):

    # Add bias column
    X_aug = np.column_stack((X, np.ones(X.shape[0])))

    # Solve least squares
    params = np.linalg.lstsq(X_aug, y, rcond=None)[0]

    W_out = params[:-1]
    b_out = params[-1]

    return W_out, b_out