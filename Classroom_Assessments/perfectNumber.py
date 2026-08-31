n=int(input("Enter a number to check if it is a perfect number: "))
if n <= 1:
    print("The number is not a perfect number.")
else:
    divisor_sum = 1
    for i in range(2, n):
        if n % i == 0:
            divisor_sum += i
    if divisor_sum == n:
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")