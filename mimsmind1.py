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


def get_bulls_and_cows(magic_number_split, guess_split):
    """ Takes the magic number and user guess split into a list of digits
        and calculates bulls and cows
        Bull - The number of values that are equal in a given position on both the lists
        Cows - All the values in the guess list present in the magic number list, minus the bulls
        TODO : Ask about how it plays out when the guess is something like 444 and the magic number is 423
    """
    bulls = len([i for i, j in zip(magic_number_split, guess_split) if i == j])  # zip returns a tuple of the i-th element in the lists
    cows = len([i for i in guess_split if i in magic_number_split]) - bulls

    return bulls, cows


def play_game(n):
    """ Gets user input and checks against magic number until the user
        correctly guesses the magic number or exhausts tries.
    """
    max_tries = (n*n) + n  # Equation for max number of tries
    tries = 0
    magic_number = generate_random(n)
    magic_number_split = list(str(magic_number))
    
    # Welcome message
    print("Let's play the mimsmind1 game. You have {} guesses".format(max_tries))
    # Get and validate user's first guess
    while True:
        try:
            guess = int(input("Guess a {}-digit number: ".format(n)))
            break
        except:
            print("Invalid input. Try again: ")
    # Returns number of cows and bulls till tries are exhausted
    while tries < max_tries:
        guess_split = list(str(guess)) 
        # Winning condition
        if magic_number == guess:
            tries += 1
            print("Congratulations. You guessed the correct number in {} tries.".format(tries))
            break
        # Constraint 1 -  If number of digits in guess and magic number are not the same, try again
        if len(magic_number_split) != len(guess_split):  
            try:
                guess = int(input("Invalid input, try again: "))
            except:
                continue  # Continue till users enters valid integer input, guess still retains old value when exception occurs, so this works
        # Get cows and bulls for a valid n digit input
        else:
            tries += 1
            bulls, cows = get_bulls_and_cows(magic_number_split, guess_split)
            try:
                guess = int(input("{} bull(s), {} cow(s). Try again: ".format(bulls, cows)))
            except:
                guess = int(input("Invalid input, try again: "))
    # When the user exhausts all the tries without guessing correctly
    else:
        print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(max_tries, magic_number))


def main():
    try:
        n = int(sys.argv[1])  # Number of digits in the random no.- uses command line input if valid, else defaults to 1
        play_game(n)
    except:
        play_game(3)

if __name__ == "__main__":
    main()
