import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape:
		raise ValueError("Both input vectors must have the same shape.")
	
	dot_product = np.dot(v1, v2)

	magnitude_v1 = np.linalg.norm(v1)
	magnitude_v2 = np.linalg.norm(v2)

	if magnitude_v1 == 0 or magnitude_v2 == 0:
		raise ValueError("Input vectors cannot be empty or have zero magnitude.")
	
	return float(dot_product/ (magnitude_v1 *magnitude_v2))
	pass