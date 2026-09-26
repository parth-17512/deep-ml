import numpy as np

def linear_regression_normal_equation(
    X: list[list[float]],
    y: list[float]
) -> list[float]:

    # Convert lists into NumPy arrays
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # Normal equation:
    # theta = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    # Round each coefficient to 4 decimal places
    return [round(float(coef), 4) for coef in theta]