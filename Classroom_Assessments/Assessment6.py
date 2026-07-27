sum=0
while True:
    user_input=int(input("Enter a number between 1 to 100: "))
    if user_input==999:
        break
    elif user_input==-1:
        continue
    elif user_input<1 or user_input>100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    else:
        sum=sum + user_input

print("The sum of the numbers entered is:", sum)



