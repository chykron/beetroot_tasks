"""
Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.
# I choose to use my own exercises:
"""


def add(x: int | float, y: int | float) -> int | float:
    """Func to add two nums"""
    return x + y


def is_palindrome(word: str) -> bool:
    """Func to check if the word is a palindrome"""
    if word == word[::-1]:
        return True
    else:
        return False
