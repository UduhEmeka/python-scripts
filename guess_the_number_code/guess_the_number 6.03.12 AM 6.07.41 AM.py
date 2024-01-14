import random
import os
from guess_the_number_art import guess_the_number_logo

# Constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
SECRET_NUMBER_RANGE = (0, 100)

def clear():
    """Clears the screen."""
    if os.name == 'nt':
        _ = os.system('cls')        # For Windows
    else:
        _ = os.system('clear')      # For macOS and Linux

def compare_number(secret, guess, attempts):
    """Compares user's guess with secret_number and determines if the game has been won."""
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"You got it! The answer was {secret}.")
        return True

    print(f"You have {attempts} attempts remaining to guess the number.")
    return False

def set_difficulty():
    """Sets the difficulty level and returns the number of attempts."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_LEVEL_ATTEMPTS if level == "easy" else HARD_LEVEL_ATTEMPTS

def get_user_guess():
    """Gets the user's guess, handling non-integer inputs."""
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    """Main function to play the number guessing game."""
    print(guess_the_number_logo)
    print("Welcome to the Number Guessing Game!")
    print("I have a secret number in mind. Your task is to guess the number before you run out of attempts.")
    print(f"Hint: The secret number is somewhere between {SECRET_NUMBER_RANGE[0]} and {SECRET_NUMBER_RANGE[1]}")

    secret_number = random.randint(*SECRET_NUMBER_RANGE)            # The asterisk unpacks the tuple, providing its elements as separate arguments to the randint function.
    attempts = set_difficulty()                                     # If you remove the asterisk and directly pass SECRET_NUMBER_RANGE without unpacking, you will get a TypeError.
                                                                    # This is because randint would be receiving a single argument (the tuple) instead of two separate arguments.
    game_won = False
    while not game_won and attempts > 0:
        attempts -= 1
        guessed_number = get_user_guess()
        game_won = compare_number(secret_number, guessed_number, attempts)

    if not game_won:
        print(f"Sorry, you lost as you have exhausted your attempts. The correct number was {secret_number}.")


while input("Do you want to play the guessing game? Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()