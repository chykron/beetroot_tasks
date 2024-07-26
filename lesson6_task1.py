"""
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""
from random import randint

my_list = []

while len(my_list) < 10:
    my_list.append(randint(1, 100))
    if len(my_list) == 10:
        print(max(my_list))
print(my_list)
