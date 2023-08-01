import random
from re import A

def GuessingGame():
    running = True
    upper = int(input("Enter Upper limit: "))
    print('Your range is 1-', upper)
    n = random.randrange(1,upper)
    guess = int(input("Enter any number above 1: "))
    while running == True:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))
        else:
            running = False
        print("you guessed it right!!")
        again = print(input('Do you want to play again? (Y/N)'))
        if again == 'y' or 'Y':
            GuessingGame()
        elif again == 'n' or 'N':
            break
print('Thank you!')
            
GuessingGame()
