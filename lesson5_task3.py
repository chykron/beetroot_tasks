"""
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input
string. For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
that combine characters 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

Tips: Use random module to get random char from string)
"""
import random

input_str = input("Enter a string: ")
for example in range(5):
    # convert a str to a list, so we'll get a list of characters to work with
    characters = list(input_str)
    # shuffle the characters in any order
    random.shuffle(characters)
    # join method concatenates a list characters into a srt
    shuffled_string = ''.join(characters)
    # we got exactly 5 printed instances of shuffled_string under example for loop
    print(shuffled_string)
