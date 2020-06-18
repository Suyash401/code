user_data = {}

def register():
	username = input("Enter your username: ")
	if username in user_data:
		print("This username is already taken. Please try again.")
		return register()
	else:user_data = {}

def register():
	username = input("Enter your username: ")
	if username in user_data:
		print("This username is already taken. Please try again.")
		return register()
	else:
		password = input("Enter your password: ")
	user_data.update({username:password})
	print("Registered Successfully. You can now login")
	login()

def login():
	username = input("Enter your username: ")
	if username in user_data:
		password = input("Enter your password: ")
		if user_data[username] == password:
			print("Access Granted")
		else:
			print("Incorrect Password. Try Again or Register ")
	else:
		retry = input("Username not found. Try again or Register: ")
		if retry.lower() in ['register','r']:
			register()
		else:
			login()
while True:
	action = input("Do you want to login or register: ").lower()
	if action == 'login':
		login()
		break
	elif action == 'register':
		register()
		break
	else:
		print("Invalid Input. Try again.")



		password = input("Enter your password: ")
	user_data.update({username:password})
	print("Registered Successfully. You can now login")
	login()

def login():
	username = input("Enter your username: ")
	if username in user_data:
		password = input("Enter your password: ")
		if user_data[username] == password:
			print("Access Granted")
		else:
			print("Wrong Password")
	else:
		retry = input("Username not found. Try again or Register: ")
		if retry.lower() in ['register','r']:
			register()
		else:
			login()
while True:
	action = input("Do you want to login or register: ").lower()
	if action == 'login':
		login()
		break
	elif action == 'register':
		register()
		break
	else:
		print("Invalid Input. Try again.")


