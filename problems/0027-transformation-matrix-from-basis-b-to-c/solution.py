import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B,dtype=float)
	C = np.array(C,dtype=float)

	inv_c = np.linalg.inv(C)
	P = inv_c @ B 
	return P.tolist()