import random

generated_number=random.randint(1, 100)
Number__of_attempts = 5
while Number__of_attempts > 0:
    user_input = input("Guess the number between 1 and 100 : ")

    guess = int(user_input)
    Number__of_attempts -= 1

    if guess == generated_number:
        print("Congratulations! You guessed the number correctly.")
        break
    elif guess < generated_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

if Number__of_attempts == 0:
    print("Sorry, you've run out of attempts. The number was:", generated_number)