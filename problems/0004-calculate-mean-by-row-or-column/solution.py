def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	row_size = len(matrix[0])
	col_size = len(matrix)
	if mode == 'row':
		for row in matrix:
			means.append(sum(row) / row_size)
	elif mode == 'column':
		for col in zip(*matrix):
			means.append(sum(col) / col_size)
	
	return means