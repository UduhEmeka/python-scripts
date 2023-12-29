from black_jack_art import blackjack_logo
import random
import os

def clear():
    """Clears the console."""                                                           # However, in order for this functionality to work in pycharm, you need to enable "Emulate terminal in output console".
    if os.name == 'nt':                                                                 # You can find this when you right-click the file you want to add this function to and select "modify run configuration".
        _ = os.system('cls')           # For Windows
    else:
        _ = os.system('clear')         # For macOS and Linux

def deal_card():
    """Returns a random card from the deck."""
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_list)
    return card

def calculate_score(player_cards):
    """Returns the sum of elements in a list."""
    if sum(player_cards) == 21 and len(player_cards) == 2:                              # Inside calculate_score() check for a blackjack and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        return 0
    if 11 in player_cards and sum(player_cards) > 21:                                   # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)

def compare(user_score, computer_score):
    """Compares the scores of two players."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(blackjack_logo)
    user_cards = []                                                                             # Initialize an empty Card list for the User.
    computer_cards = []                                                                         # Initialize an empty Card list for the Computer.
    user_score = None                                                                           # Initializing a user score with the variable "None"
    computer_score = None                                                                       # Initializing a computer score with the variable "None"

    for i in range(2):                                                                          # Deals 2 cards each to the user and computer.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False                                                                        # Initializes the while loop with game over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)                                                # Calculates the Users score.
        computer_score = calculate_score(computer_cards)                                        # Calculates the Computers score.
        print(f"   Your cards: {user_cards}, current score: {user_score}")                      # Shows the User's cards and User's score
        print(f"   Computer's first card: {computer_cards[0]}")                                 # Shows the Computer's score

        if user_score == 0 or computer_score == 0 or user_score > 21:
            clear()
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")        # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                clear()
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))                                                  # Shows the result of comparison between the User and Computer's score

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
