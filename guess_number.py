import random
number = random.randint(1,100)

def start():
    guess = None
    number_of_guess = 0
    while(guess!=number):
        number_of_guess += 1 
        if(number_of_guess<=1):
            s="enter your number"
        else:
            if(guess>number):
                s="Wrong! Enter lower number"
            else:
                s="Wrong! Enter higher number"
        try:
            guess = int(input(f"{s}: "))
        except Exception as e:
            print(e)

    print(f"congratulations, your have guessed it...!!! in {number_of_guess} times")
    
start()