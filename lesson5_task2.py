"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
"Hello <name>, on your next birthday you’ll be <age+1> years"
"""
name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"Hello {name.title()}, on your next birthday you’ll be {age + 1} years old!")
