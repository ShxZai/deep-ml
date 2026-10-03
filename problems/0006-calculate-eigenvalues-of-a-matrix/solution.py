import math

def quadfor(a, b, c):
	return [(-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a)]

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	roots = quadfor(1, trace*-1, det)
	return sorted(roots, reverse=True)