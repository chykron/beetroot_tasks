"""
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def outer_function(message: str) -> str:
    def inner_function():
        return f"This is inner message and this is '{message.lower()}'"

    return inner_function()


my_func = outer_function("Outer Message!")
print(my_func)
