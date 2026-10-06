def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		means= []

		for row in matrix:
			mean = sum(row)/len(row)
			means.append(mean)
		return means 

	elif mode == "column":
		means= []

		no_of_cols = len(matrix[0])

		for j in range(no_of_cols):
			col_sum = 0

			for i in range(len(matrix)):
				col_sum += matrix[i][j]

			mean = col_sum/len(matrix)
			means.append(mean)
		return means
