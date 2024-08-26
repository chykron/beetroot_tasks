"""
Write a Python program to detect the number of local variables declared in a function.
"""


def local_variables(func) -> int:
    return func.__code__.co_nlocals


def test_local_variables() -> None:
    a = 1
    b = 2
    c = 3
    return None


print(local_variables(test_local_variables))
