""" Code guessing game """

"""
The program will generate a code of three 0-9 unrepeated
numbers which you have to guess.
If a guessed number matches the exact number and position in
the target code, then the program hints you with 'Bullseye!'.
If a guessed number matches one number but it is not in the
correct position in the code list, then you will get a
'Missed!' hint.
If you did not guess any correct number regardless its
position, a 'Nothing' hint will be displayed.
If the code matches your guess, you win!
E.g.:
Code: 123   Guess: 124  Hints: Bullseye! Bullseye! Nothing!
Code: 476   Guess: 123  Hints: Nothing! Nothing! Nothing
Code: 365   Guess: 564  Hints: Missed! Bullseye! Missed!
Code: 729   Guess: 729  Hints: You got it! It was 729!
"""

import sys
import random


def game_flow():
    """ Creates and fills up a list with three random str-casted
    values which will be the code to guess. Then, asks the user
    for the guess and show hints until they find out which was
    the code. """

    code = []
    guess = []

    # Random 3-number code generation
    # Fill up code list with an array of three
    # unrepeated 0-9 numbers casted to str
    while len(code) < 3:
        rnd = random.randint(0, 9)

        if str(rnd) not in code:
            code.append(str(rnd))

    while True:

        # User input for the code guess.
        # Fills up the guess list with an array of
        # three unrepeated 0-9 numbers casted to str.
        guess = list(input("Guess a 3 digit code (q to quit): "))

        if guess == ['q']:
            sys.exit()
        elif len(guess) is not 3:
            print('3 digit code, plz')
            continue
        elif isRepeatedNumber(guess):
            print('No repeated numbers, plz')
            continue

        # if both lists are equal, it's a match, so
        # return out of game_flow()
        if code == guess:
            print(f'You got it! It was {"".join(code)}!')
            return

        # Show the hints for each of the values by
        # comparing both lists
        for i in range(len(code)):
            if code[i] == guess[i]:
                print('Bullseye!')
            elif guess[i] in code:
                print('Missed!')
            else:
                print('Nothing!')


def play_again():
    """ Ask the user to play again and restart the
    game if so. """
    while True:
        option = input('Play again? (y/n) ').lower()
        if option == 'n':
            sys.exit()
        elif option == 'y':
            return main()


def isRepeatedNumber(string):
    """ Returns True if any value in the list passed
    as a parameter repeats itself """
    for i in string:
        if string.count(i) > 1:
            return True


def main():
    """ Launch the game and prompt to play again if
    the game ends. """
    game_flow()
    play_again()


if __name__ == '__main__':
    main()
