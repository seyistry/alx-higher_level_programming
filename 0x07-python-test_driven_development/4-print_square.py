def print_square(size):
	"""_summary_

	Args:
		size (_type_): _description_
	"""
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	elif size < 0:
		raise ValueError("size must be >= 0")
	else:
		for i in range(size):
			print(f"{'#' * size}")