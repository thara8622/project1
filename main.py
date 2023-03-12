#Create a function that generates random password, input is the length of the password
import random


def random_pass(passlen= int(input("Enter your prefer password lenght:"))):
    alphabets = "abcdefghijklmnopqrstuvwxyz1234567890"
    result = ""
    for _ in range(passlen):
        result = result + str(alphabets[random.randrange(0,passlen-1)])
    return result


print(random_pass())