# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:33:03 2020

@author: Abraham
"""

# Remember, if you don't run the entire code at the same time, you could easily cheat.

import numpy as np

actual=np.random.randint(low=10) # the actual number
guess1=int(input("Make a first guess ")) # your guess

if guess1==actual:
    print("Your first guess was correctly")
else:
    if guess1 > actual:
        print("Your first guess was the wrong number and the actual number is lower than your guess")
    else:
        print("Your first guess was the wrong number and the actual number is greater than your guess")
    guess2=int(input("Make a second guess ")) # your second guess
    if guess2==actual:
        print("Your second guess was correctly")
    else:
        if (abs(actual-guess2)<=3 and actual<guess2):
            print("Your second guess was wrong but the actual number is at most 3 away from your guess and lower than your guess")
        elif (abs(actual-guess2)<=3 and actual>guess2):
            print("Your second guess was wrong but the actual number is at most 3 away from your guess and higher than your guess")
        elif (abs(actual-guess2)>3 and actual<guess2):
            print("Your second guess was wrong and the actual number is more than 3 away from your guess and lower than your guess")
        else:
            print("Your second guess was wrong and the actual number is more than 3 away from your guess and higher than your guess")
        guess3=int(input("Make a final guess ")) # your final guess
        if guess3==actual:
            print("Your final guess was correctly")
        else:
            print("You guessed wrong and you have run out of guesses. The actual number is ", actual)

















