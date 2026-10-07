def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		mean = []
		 
		for row in matrix:
			total = 0
			for values in row:
				total += values
			mean.append(total/len(row))
		return mean
			
		
	if mode == "column":
		mean = []
		 
		for j in range(len(matrix[0])):
			total = 0
			for i in range(len(matrix)):
				total += matrix[i][j]
			mean.append(total/len(matrix))
		return mean
			