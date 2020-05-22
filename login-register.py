import mysql.connector
from passlib.hash import pbkdf2_sha256
from getpass import getpass

#Establishing Connection with MySQL Server
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)
cursor = conn.cursor()

# Check if database exists, if it doesn't then prepare it
try:
    cursor.execute("create database codinground")
    print("Setting Up Database. Please wait a minute.")
    cursor.execute("use codinground")
    print("Setting up tables")
    cursor.execute("create table users(id int not null primary key auto_increment,name varchar(20) not null,username varchar(20) unique,password varchar(100) not null)")
    print("Database is ready\n")
except:
    cursor.execute("use codinground")
    pass

#Registration Function    
def register():
    name = input("Please Enter Your Name: ")
    query = "SELECT * from users where username="

    #Checks if the username is already registered or not
    while True:     
        username=input("Please enter your Username: ")
        tmp_query=query+'"'+username+'"'
        cursor.execute(tmp_query)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Username alerady taken. Please try again.")
        else:
            break
    password1 = getpass()
    #Encrypts Password
    password1 = pbkdf2_sha256.encrypt(password1, rounds=200000, salt_size=16)
    cmd = "insert into users(name,username,password) values (%s,%s,%s)"
    data = (name,username,password1)
    try:
        cursor.execute(cmd,data)
        conn.commit()
        print("Registration Successful")
    except:
        conn.rollback()
        print("Unable to register")

#Login Function
def login():
    query = "SELECT username from users where username="
    while True:     
        username=input("Please enter your Username: ")
        tmp_query=query+'"'+username+'"'
        cursor.execute(tmp_query)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Username Does not exist please try again.")
        else:
            username = result[0][0]
            break
    query2 = "select password from users where username=" 
    tmp_query=query2+'"'+username+'"'
    cursor.execute(tmp_query)
    passwordretrieved = cursor.fetchone() 
    passwordretrieved = passwordretrieved[0]
    while True:
        password2 = getpass()
        passcheck = pbkdf2_sha256.verify(password2, passwordretrieved)
        if passcheck:
            print("Logged in Successfully")
        else:
            print("Incorrect Password. Try Again")

#User Input For Login or Register
while True:
    login_register = input("Login or Register\n")
    if login_register.lower() == "register":
        register()
        break
    elif login_register.lower() == "login":
        login()
        break
    else:
        print("Invalid Input")

#Closing Connection with Database
cursor.close()
conn.close()
