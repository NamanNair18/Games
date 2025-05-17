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
