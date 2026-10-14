import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	x= np.array(x,dtype=float)
	y= np.array(f(x.tolist()),dtype=float)
	J= np.zeros((len(y),len(x)))

	for j in range(len(x)):
		xh = x.copy()
		xh[j] += h
		J[:, j]= (np.array(f(xh.tolist()))-y)/h
	return J.tolist()