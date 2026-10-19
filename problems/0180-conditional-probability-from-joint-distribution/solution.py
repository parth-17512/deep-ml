def conditional_probability(joint_distribution: dict) -> float:
	"""
	Compute conditional probability P(A|B) from a joint probability distribution.

	Args:
		joint_distribution (dict): dictionary with keys ('A','B'), ('A','`B'), ('`A','B'), ('`A','`B')

	Returns:
		float: Conditional probability P(A|B)
	"""
	A_intersection_B= joint_distribution[('A','B')]
	probability_B = joint_distribution[('A','B')]+joint_distribution[('`A','B')]
	total=0
	for values in joint_distribution:
		total += joint_distribution[values]
	if total == 1.0:
		if probability_B > 0:
			return float(A_intersection_B/probability_B)
		else:
			return 0.0
	return 0.0

	
