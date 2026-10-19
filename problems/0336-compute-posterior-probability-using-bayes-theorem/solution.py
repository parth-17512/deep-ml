def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	
	n = len(priors)
	result =[]
	for i in range(n):
		result.append(priors[i]*likelihoods[i])
		
	
	total = sum(result)
	for i in range(len(result)):
		result[i] = result[i]/total
	return result


