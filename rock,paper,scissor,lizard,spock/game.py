import random

win_lose_pairs = [('Scissors','Paper'),
                  ('Paper'   ,'Rock'),
                  ('Rock'    ,'Lizard'),
                  ('Lizard'  ,'Spock'),
                  ('Spock'   ,'Scissors'),
                  ('Scissors','Lizard'),
                  ('Lizard'  ,'Paper'),
                  ('Spock'   ,'Rock'),
                  ('Rock'    ,'Scissors'),]

choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

computer_choice = random.choice(choices)

print(' Please choose one of the option below: ')
print(' -> 0 for Rock\n -> 1 for Paper\n -> 2 for Scissors\n -> 3 for Lizard -> 4 for Spock')

while True:
    try:
        user_input = int(input(' Your choice (0 - 4):  '))
        if user_input not in range(5):
            raise ValueError
        break
    except ValueError:
        print('Enter number only')

human_choice = choices[user_input]

if computer_choice == human_choice:
    result = 'Draw!'

elif (human_choice, computer_choice) in win_lose_pairs:
    result = 'You won!'

else:
    result = 'You Lost!'

print('--------------------------------------')
print(' > You Chose      : ',human_choice)
print(' > Computer Chose : ', computer_choice)
print(' > Result         : ', result)
print('--------------------------------------')

play_again = input('Play again (Y/N): ')
if play_again.lower() == 'n':
    break 