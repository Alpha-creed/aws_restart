#game intro
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#library importaion
import random

#assign random number to the variable number
number = random.randint(1,10)

#assign boolean to the isGuessRight
isGuessRight = False
#loop through till the is GuessRight vaible is true
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        