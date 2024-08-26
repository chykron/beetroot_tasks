"""
Write a decorator arg_rules() that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    pass
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""

from typing import Callable, List
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: List[str]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args) -> bool:
            # Iterate over each argument to reach the requirements
            for arg in args:
                # Check by type
                if not isinstance(arg, type_):
                    print(f"Argument type is {type(arg).__name__}; expected {type_.__name__}")
                    return False

                # Ensure the argument supports len() if it is a str, otherwise it's not working
                if isinstance(arg, str):

                    if len(arg) > max_length:
                        print(f"Argument length is {len(arg)}; expected {max_length}")
                        return False

                # Check if it contains all required substrings
                if not all(substring in arg for substring in contains):
                    print(f"Argument must contain: {', '.join(contains)}")
                    return False

            return func(*args)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
