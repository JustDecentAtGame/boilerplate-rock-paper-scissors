# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
import pandas as pd

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    PREPROCESSING = {'R': 0, 'P': 1, 'S': 2, '':4}
    guess = random.choice(['R', 'P', 'S'])
    with open('Game_Rounds.csv', 'a') as f:
        f.write(f"{PREPROCESSING.get(guess)},{PREPROCESSING.get(prev_play)}\n")

    df = pd.read_csv('Game_Rounds.csv', columns=['guess', 'prev_play'])
    if len(opponent_history) > 2:
    
    return guess
