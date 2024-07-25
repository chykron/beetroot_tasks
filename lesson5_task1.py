"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

from random import randint

number = randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == number:
    print("You won!")
else:
    print(f"You lost! The number was {number}")
