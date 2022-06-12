"""Bagels, by Al Sweigart al@inventwithpython.com
2. A deductive logic game where you must guess a number based on clues.
3. View this code at https://nostarch.com/big-book-small-python-projects
4. A version of this game is featured in the book "Invent Your Own
5. Computer Games with Python" https://nostarch.com/inventwithpython
6. Tags: short, game, puzzle

I copied this cuz I am lazy and this wouldn't teach me anything!"""

#Ideas: Repeat instructions?

import random

num_digits = 3 # (!) Try setting this to 1 or 10.
max_guesses = 10 # (!) Try setting this to 1 or 100.


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

    while True: #main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break #They're correct, so break out of this loop.        
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_num))

        # Ask player if they want to play again. 
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    

def get_secret_num():
    """Returns a string made up of num_digitis unique random digits."""
    numbers = list('0123456789') #Create a list of digits 0 to 9
    random.shuffle(numbers) #Shuffle them into a random order

    # Get the first num_digits digits in the list for the secret number:
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' #There are no correct digits at all. 
    else:
        # Sort the clues into alphabetical order so their original order
        #doesn't give information away.
        clues.sort()
        # Make a signle string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

#questions
"""
1. What happens when you change the NUM_DIGITS constant? 

2. What happens when you change the MAX_GUESSES constant?

3. What happens if you set NUM_DIGITS to a number larger than 10?

4. What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?

5. What error message do you get if you delete or comment out numGuesses = 1 on line 34?

6. What happens if you delete or comment out random.shuffle(numbers) on line 62?

7. What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?

8. What happens if you comment out numGuesses += 1 on line 44?
You will enter an infinite loop. It would never result into a True value and therefor keep running. 
"""