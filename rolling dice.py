import random
while True:
    print("1. Roll the dice\n2. Exit")
    userchoice = int(input("What do you want to do?\n"))   
    if userchoice == 1:
        answer = random.randint(1,6)
        print(f"Your random number is {answer}")
    else:
        break