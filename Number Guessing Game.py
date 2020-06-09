import random
print("Number Guessing Game")
number = random.randint(1,10)
guess = int(input("Guess the number: "))
if guess > number:
	print("Guess Lower")
elif guess < number:
	print("Guess Higher")
else:
	print("You Won")
print(number)
