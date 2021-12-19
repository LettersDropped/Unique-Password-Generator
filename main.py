import string 
import random

chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    user_input = int(input("Enter the length of the password: "))

    password = []
    for i in range(user_input):
        password.append(random.choice(chars))

    random.shuffle(password)
    print("".join(password))
    

password_generator() 

