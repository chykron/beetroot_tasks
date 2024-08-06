"""
The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly.
"""
import random

# Generate random numbers to work with
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Generate random simple operator
operator = random.choice(['+', '-'])

# Generate the result based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2

# Ask user to solve math expression
user_answer = input(f"What is the answer for {num1} {operator} {num2}?: ")
if int(user_answer) == result:
    print("Correct!")
else:
    print("Incorrect!")
