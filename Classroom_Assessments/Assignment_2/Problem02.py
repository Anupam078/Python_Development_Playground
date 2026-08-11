"""Problem 2

Given a list of substrings and a list of strings, check for each substring if it
is present in any string of the second list.
"""

from typing import List


def substrings_in_list(subs: List[str], strs: List[str]) -> List[bool]:
	"""Return list of booleans: True if substring appears in any string in strs."""
	result = []
	for sub in subs:
		found = any(sub in s for s in strs)
		result.append(found)
	return result


if __name__ == "__main__":
	test_list1 = ["Gfg", "is", "best"]
	test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]
	print(substrings_in_list(test_list1, test_list2))

	test_list2b = ["I love Gfg", "It is Best for Geeks", "Gfg means CS"]
	print(substrings_in_list(test_list1, test_list2b))