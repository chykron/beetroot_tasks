"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!
"""
from typing import Callable, Any


def logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Print the function name and the args passed to it
        print(f"{func.__name__} called with {', '.join(map(str, args))}")
        # Call the original func with args
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x: int, y: int) -> int:
    return x + y


@logger
def square_all(*args: int) -> int:
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(2, 3, 4)
