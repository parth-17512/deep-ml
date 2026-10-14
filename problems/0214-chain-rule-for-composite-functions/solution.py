import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	funcs = {
		'square':(lambda x: x**2,lambda x: 2*x),
		'sin': (np.sin,np.cos),
		'exp': (np.exp,np.exp),
		'log': (np.log,lambda x: 1/x)
	}
	grad = 1.0 
	for f in reversed(functions):
		fn,df = funcs[f]
		grad *= df(x)
		x = fn(x)
	return grad