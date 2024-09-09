"""
Create a class method named validate, which should be called from the __init__ method to validate parameter email,
passed to the constructor. The logic inside the validate method could be to check if the passed email parameter
is a valid email string.
"""

import re


class Email:
    def __init__(self, email: str) -> None:
        self.email = email
        self.validate(email)

    @classmethod
    def validate(cls, email: str) -> str:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address")
        return email


try:
    user = Email("oleh.perehuda@beetroot.se")
except ValueError as e:
    print(e)
