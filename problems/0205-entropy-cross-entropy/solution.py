import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
	"""
	entropy = 0.0
	cross_entropy = 0.0

	for p,q in zip(P,Q):
		if p == 0:
			continue

		entropy -= p*np.log(p)

		if q == 0 :
			cross_entropy = float('inf')
		elif cross_entropy != float('inf') :
			cross_entropy -= p*np.log(q)
	return float(entropy),float(cross_entropy)



