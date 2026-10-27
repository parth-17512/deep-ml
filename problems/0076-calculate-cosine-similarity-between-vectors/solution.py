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
	a= np.array(v1,dtype=float)
	b= np.array(v2,dtype=float) 

	if a.shape != b.shape or a.size ==0:
		return -1 
	if np.linalg.norm(a) == 0 or np.linalg.norm(b)==0:
		return -1 
	return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))