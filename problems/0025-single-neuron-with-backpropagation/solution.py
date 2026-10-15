import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	w = initial_weights.astype(float).copy()
	b= float(initial_bias)
	mse_values = []

	for _ in range(epochs):
		p = 1/(1+np.exp(-(features @ w+b)))
		e = p - labels
		mse_values.append(round(float(np.mean(e**2)), 4))

		dz = 2*e*p*(1-p)
		w -= learning_rate*np.mean(dz[:,None]*features, axis=0)
		b -= learning_rate*np.mean(dz)
	return np.round(w, 4), round(b, 4), mse_values