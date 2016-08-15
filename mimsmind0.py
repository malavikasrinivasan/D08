#  Imports
import sys
from random import randint

# Body

def generate_random(n):
    """ Generates an n-digit random integer
    TODO : Zero currently not included when n = 1
    """
    lower_bound = 10**(n-1)
    upper_bound = (10**n)-1
    return randint(lower_bound, upper_bound)


def play_game(n):
    """ Gets user input and checks against magic number until the user
        correctly guesses the magic number
    """
    tries = 0
    magic_number = generate_random(n)
    print("Let's play the mimsmind0 game.")
    # Get and validate user's first guess
    while True:
        try:
            guess = int(input("Guess a {}-digit number: ".format(n)))
            tries += 1
            break
        except:
            print("That is not a valid number, try again.")   
    while True:
        # Check guess against magic number and give directional guidance if incorrect
        try:
            if magic_number > guess:
                guess = int(input("Try again. Guess a higher number: "))
                tries += 1
            elif magic_number < guess:
                guess = int(input("Try again. Guess a lower number: "))
                tries += 1
            else:
                print("Congratulations. You guessed the correct number in {} tries.".format(tries))
                break
        except:
            print("That's not a valid number.")


def main():
    try:
        n = int(sys.argv[1])  # Number of digits in the random no.- uses command line input if valid, else defaults to 1
        play_game(n)
    except:
        play_game(1)

if __name__ == "__main__":
    main()
