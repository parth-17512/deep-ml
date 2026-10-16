
import numpy as np

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
) -> tuple[np.ndarray, float, list[float]]:

    w = initial_weights.astype(float).copy()
    b = float(initial_bias)
    mse_values = []

    m = len(labels)

    for _ in range(epochs):
        # 1. Calculate predictions
        z = features @ w + b
        p = 1 / (1 + np.exp(-z))

        # 2. Calculate and store loss before updating
        e = p - labels
        mse = np.mean(e ** 2)
        mse_values.append(round(float(mse), 4))

        # 3. Calculate gradients
        dz = 2 * e * p * (1 - p)
        dw = (features.T @ dz) / m
        db = np.sum(dz) / m

        # 4. Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db

    return np.round(w, 4), round(b, 4), mse_values
