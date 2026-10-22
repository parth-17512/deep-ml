import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trance = matrix[0][0]+matrix[1][1]
	det = (matrix[0][0]*matrix[1][1]) -(matrix[1][0]*matrix[0][1])
	eigenvalue = np.roots([1,-trance,det])
	return eigenvalue.tolist()