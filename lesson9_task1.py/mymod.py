"""
Basics, import, work with os module

Write a program that counts lines and characters in a file.
Create a Python module called mymod.py, which has three functions:
count_lines(name) function that reads an input file and counts the number of lines in it
count_chars(name) function that reads an input file and counts the number of characters in it
test(name) function that calls both counting functions with a given input filename.

All three mymod.py functions should expect a filename string to be passed in.
Test your module interactively, using import and name qualification to fetch your exports.
"""


def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        chars = file.read()
        return len(chars)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"File '{name}' has {lines} lines and {chars} characters")


# didn't want to create a separate file for the test, tested mymod.py interactively inside the terminal:
# import mymod
# mymod.test("my_file.txt")
