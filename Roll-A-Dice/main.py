import random

def rollDices(dices):
    for i in range(1, dices+1):
        print(f"Dice {i} Rolled: ", random.randint(1, 6))

dices = int(input("How many dices you want to roll?"))

wannaRoll = "yes"

while(wannaRoll.lower() == 'yes' or wannaRoll.lower() == 'y'):
    rollDices(dices)
    wannaRoll = input("Do you want to Roll A Dice again? (Yes/No): ")