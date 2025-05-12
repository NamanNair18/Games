import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'happy', 'Rihno', 'Crate', 'Coding']

print("Welcome to the Word Guessing Game!")
print("You have 10 attempts to guess the word. Guess one letter at a time. Good luck!")

word = random.choice(word_bank) #used to select a random word from the world_bank

guessedword = ['_'] * len(word)
attempts = 10
while attempts > 0:
    print('\n Current Word: ' + ' ' .join(guessedword))
    guess = input('Guess the Letter: ')

    if guess in word: # Check if the guessed letter is present in the chosen word
        for i in range (len(word)):
            if word[i] == guess:
                guessedword[i] = guess
                print('Great Guess!!')
    else: # If the guessed letter is not in the word
        attempts -= 1
        print('Wrong guess! Attempts Left: ' + str(attempts))

    if '_' not in guessedword: # Check if there are no underscores left, meaning the word is fully guessed
        print('\n Congratulations !! You guessed the Word: ' + word)
    break
else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
