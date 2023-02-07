import re

email = input("what's your email?")

if re.search("@" and ".", email):
    print("Valid")
else:
    print("Invalid")

