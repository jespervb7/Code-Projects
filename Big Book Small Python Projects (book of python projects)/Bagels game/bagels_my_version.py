"""Bagels, by Al Sweigart al@inventwithpython.com
2. A deductive logic game where you must guess a number based on clues.
3. View this code at https://nostarch.com/big-book-small-python-projects
4. A version of this game is featured in the book "Invent Your Own
5. Computer Games with Python" https://nostarch.com/inventwithpython
6. Tags: short, game, puzzle

I copied this cuz I am lazy and this wouldn't teach me anything!"""

import random

num_guesses = 10
num_digits = 3

def main():
     print(''''Bagels, a deductive logic game. 
    By Al Sqeigart al@inventwithpython.com
    
    I am thinking of a {}-digit number with no repeated digits.
    try to guess what it is. Here are some clues:
    When I say: 	That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.
        
        For example, if the secret number was 248 and your quess was 843, the clues would be Fermi Pico.'''.format(num_digits))
    #while True: #main loop. Needs a break statement to quit looping. 
#get secretnumber function

#get clues function

if __name__ == '__main__':
    main()