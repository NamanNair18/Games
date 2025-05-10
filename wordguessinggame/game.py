import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'happy', 'Rihno', 'Crate', 'Coding']

word = random.choice(word_bank)#used to select a random word from the world_bank

guessedword = ['_'] * len(word)
attempts = 10
while attempts > 0:
    print('/n Current Word: ' + ' ' .Join(guessedword))

