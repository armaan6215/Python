import random
number = random.randint(1,100)

def start():
    guess = None
    number_of_guess = 0
    while(guess!=number):
        number_of_guess += 1 
        guess = int(input("enter your number: "))
        if(guess>number):
            print("enter lower number")
        else:
            print("enter higher number")
    print(f"congratulations, your have guessed it...!!! in {number_of_guess} times")
    
start()