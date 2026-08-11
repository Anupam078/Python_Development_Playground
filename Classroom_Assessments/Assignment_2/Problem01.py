"""Problem 1

Left and right rotations of a string.
"""

def left_rotate(s: str, d: int) -> str:
	"""Return string left-rotated by d positions."""
	if not s:
		return s
	n = len(s)
	d = d % n
	return s[d:] + s[:d]


def right_rotate(s: str, d: int) -> str:
	"""Return string right-rotated by d positions."""
	if not s:
		return s
	n = len(s)
	d = d % n
	return s[-d:] + s[:-d]


if __name__ == "__main__":
	s = "GeeksforGeeks"
	d = 2
	print("Left Rotation :", left_rotate(s, d))
	print("Right Rotation :", right_rotate(s, d))

	s2 = "qwertyu"
	d2 = 2
	print("Left rotation :", left_rotate(s2, d2))
	print("Right rotation :", right_rotate(s2, d2))

