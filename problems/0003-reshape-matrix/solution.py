import numpy as np
import math

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	arr = np.array(a)
	if math.prod(arr.shape) != math.prod(new_shape):
		return []
	arr = arr.reshape(*new_shape)
	arr.tolist()
	return arr