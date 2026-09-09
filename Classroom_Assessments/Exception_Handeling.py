try:
    num=int(input("Enter Numerator value:"))
    den=int(input("Enter denominator value:"))
    result=num/den
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid Input")
else:
    print("The result is:", result)
finally:
    print("Execution Completed")