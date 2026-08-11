"""Problem 3

Return the value for key K from the dictionary only if K is present in both
the provided list and the dictionary. Otherwise return None.
"""

from typing import Any, Dict, List, Optional


def get_value_if_in_list(test_list: List[str], test_dict: Dict[str, Any], K: str) -> Optional[Any]:
	if K in test_list and K in test_dict:
		return test_dict[K]
	return None


if __name__ == "__main__":
	test_list = ["Gfg", "is", "Good", "for", "Geeks"]
	test_dict = {"Gfg": 5, "Best": 6}
	print(get_value_if_in_list(test_list, test_dict, "Gfg"))

	test_list2 = ["Good", "for", "Geeks"]
	print(get_value_if_in_list(test_list2, test_dict, "Gfg"))
