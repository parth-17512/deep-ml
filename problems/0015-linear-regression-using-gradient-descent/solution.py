import numpy as np

def linear_regression_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float,
    iterations: int
) -> np.ndarray:

    m, n = X.shape

    # Initialize weights to zero
    theta = np.zeros(n)

    for _ in range(iterations):

        # Make predictions
        predictions = X @ theta

        # Calculate error
        error = predictions - y

        # Calculate gradient
        gradient = (1 / m) * (X.T @ error)

        # Update weights
        theta = theta - alpha * gradient

    return theta