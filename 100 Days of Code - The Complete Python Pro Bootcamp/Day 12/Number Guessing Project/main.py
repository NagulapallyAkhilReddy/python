import random

import art
# i believe my version is better than mam's version in solution.py
def lets_play(lifes):
    """will let the user play, until they have enough attempts"""
    while lifes>0:
        print(f"you have {lifes} attempts remaining to guess the number")
        guess = int(input("make a guess: "))
        lifes-=1
        if guess == number:
            print(f"you guessed it right, the number was {guess}")
            lifes=0
        elif 1 <= guess - number <= 10:
            print(f"you got it, almost there, but you are just a bit high")
        elif -10 <= guess - number <= -1:
            print(f"you are just a bit below, almost there")
        elif guess - number > 10:
            print("too high")
        elif guess - number < -10:
            print("too low")


print(art.logo)
number=random.randint(1,101)
print("welcome to the number guessing game !!")
print("I am thinking of a number between 1 and 100")
difficulty=input("choose a difficulty. type 'easy' or 'hard' : ")
if difficulty=="easy":
    attempts=10
    lets_play(attempts)
elif difficulty=="hard":
    attempts=5
    lets_play(attempts)
else:
    print("type a valid input for difficulty level")