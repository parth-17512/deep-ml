def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	cols = len(a[0])
	if cols != len(b):
		return -1
	result = []
	for i in range(len(a)):
		total = 0
		for j in range(cols):
			total += a[i][j] * b[j]
		result.append(total)
	return result
	pass