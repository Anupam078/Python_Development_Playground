def sum_and_product(a, b):
    """
    This function takes two numbers as input and returns their sum and product.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    tuple: A tuple containing the sum and product of the two numbers.
    """
    total_sum = a + b
    total_product = a * b
    return total_sum, total_product

print(sum_and_product(3, 4))  # Output: (7, 12)

sum,product = sum_and_product(5, 6)
print("Sum:", sum)        # Output: Sum: 11
print("Product:", product)  # Output: Product: 30

