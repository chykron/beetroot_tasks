"""
A Person class
Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this:
"Hello, my name is Carl Johnson and I’m 26 years old"
"""


class Person:
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        try:
            self.age = int(age)
        except ValueError:
            raise ValueError("Age must be an int")

    def talk(self) -> str:
        return f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old"


cj = Person("carl", "johnson", 26)
print(cj.talk())
