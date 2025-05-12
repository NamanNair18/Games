import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'happy', 'Rihno', 'Crate', 'Coding']

def select_word(word_bank):
    # Select a random word from the word bank
    return random.choice(word_bank)

def initialize_guessed_word(word):
    # Initialize the display word with underscores
    return ["_"] * len(word)

def is_word_guessed(display_word):
    # Check if the word is fully guessed (no underscores left)
    return "_" not in display_word

def play_game():
    # Welcome message and instructions
    print("Welcome to the Word Guessing Game!")
    print("You have 10 attempts to guess the word. Guess one letter at a time. Good luck!")

    secret_word = select_word(word_bank)
    display_word = initialize_guessed_word(secret_word)
    attempts = 10
    guessed_letters = set()

    # Main game loop
    while attempts > 0:
        print("\nCurrent Word:", " ".join(display_word))
        print("Already guessed letters:", ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

# Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
    else: # If the guessed letter is not in the word
        attempts -= 1
        print('Wrong guess! Attempts Left: ' + str(attempts))

    if '_' not in guessedword: # Check if there are no underscores left, meaning the word is fully guessed
        print('\n Congratulations !! You guessed the Word: ' + word)
    break
else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
