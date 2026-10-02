def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	scalar_multi =[]
	rows = len(matrix)
	cols = len(matrix[0])
	for i in range(rows):
		row = []
		for j in range(cols):
			row.append(scalar*matrix[i][j])
		scalar_multi.append(row)
	return scalar_multi
	pass