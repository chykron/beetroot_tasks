"""
Write a class TypeDecorators which has several methods for converting results of functions to a specified type
(if it's possible):
"""

from functools import wraps
from typing import Callable


class TypeDecorators:
    @staticmethod
    def to_int(func: Callable[[str], str]) -> Callable[[str], int]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> int:
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"{result} can't be converter to int")

        return wrapper

    @staticmethod
    def to_float(func: Callable[[str], str]) -> Callable[[str], float]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"{result} can't be converter to float")

        return wrapper

    @staticmethod
    def to_str(func: Callable[[str], str]) -> Callable[[str], str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func: Callable[[str], str]) -> Callable[[str], bool]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> bool:
            result = func(*args, **kwargs)
            if result.lower() in ("yes", "true", "1"):
                return True
            if result.lower() in ("no", "false", "0"):
                return False
            else:
                raise ValueError(f"{result} can't be converter to bool")

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


print(do_nothing('25') == 25)
print(do_something('True') is True)