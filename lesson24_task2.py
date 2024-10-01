from typing import Optional


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome.
    is_palindrome('mom')
    True
    is_palindrome('sassas')
    True
    is_palindrome('o')
    True
    is_palindrome('hello')
    False
    is_palindrome('racecar')
    True
    """
    if index >= len(looking_str) // 2:
        return True

    if looking_str[index] != looking_str[-index - 1]:
        return False

    return is_palindrome(looking_str, index + 1)
