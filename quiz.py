from inputimeout import inputimeout, TimeoutOccurred
from random import *
print("Welcome to Baisc Python Maths Quiz")
for x in range (1,11):
	operations = ['addition','multiplication','subtraction']
	question = choice(operations)
	numberone = randint(1,999)
	numbertwo = randint(1,999)
	if question == "addition":
		print(str(numberone) + "+" + str(numbertwo))
		answer = numberone+numbertwo
	elif question == "subtraction":
		print(str(numberone) + "-" + str(numbertwo))
		answer = numberone - numbertwo
	elif question == "multiplication":
		print(str(numberone) + "x" + str(numbertwo))
		answer = numberone*numbertwo
	try:
		guess = inputimeout(prompt='Enter your answer: ', timeout=10)
	except TimeoutOccurred:
		guess = "Timeout"
	if guess == answer:
		print("You won")
	elif guess == "Timeout":
		print("Your time's up")
	else:
		print("You Lose")
