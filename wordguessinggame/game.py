import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'happy', 'Rihno', 'Crate', 'Coding']

word = random.choice(word_bank)#used to select a random word from the world_bank

guessedword = ['_'] * len(word)
attempts = 10
while attempts > 0:
    print('\n Current Word: ' + ' ' .Join(guessedword))
    guess = input('Guess the Letter: ')

    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
                guessedword[i]== guess
                print('Great Guess!!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts Left: ' + str(attempts))

    if '_' not in guessedword:
        print('\n Congratulations !! You guessed the Word: ' + word)
    break
