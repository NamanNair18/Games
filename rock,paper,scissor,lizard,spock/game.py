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