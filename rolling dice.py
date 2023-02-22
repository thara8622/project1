import random 
while True:     
     print('''1. roll the dice\n2. exit     ''')    
     user = int(input("what you want to do\n"))     
     if user==1:         
        number = random.randint(1,3)         
        print(f"Your random number is {number}")     
     else:         
        break
