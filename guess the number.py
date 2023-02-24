number = 10

for i in range(3):
    userguess = int(input("Choose a number from 1 to 10\n"))
    if userguess == number:
        print(f"Bravo! the correct answer is {number}")
        break

print("You're out of guess!")