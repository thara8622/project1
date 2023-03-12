
import string
import random

def password():
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
    for length in range(passwordlen()):
        result = result + str(alphabet[random.randrange(0,passwordlen-1)])
    print(result)

def passwordlen():
    passwordlen = int(input("enter the lenght of password you prefered:\n"))
    return passwordlen
password()