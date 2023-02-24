import array as arr
import string
import random

result=""
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
passwordlen = int(input("enter the lenght of password you prefered:\n"))


for length in range(passwordlen):
    result = result + str(alphabet[random.randrange(0,passwordlen-1)])

print(result)