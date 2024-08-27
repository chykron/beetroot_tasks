"""
Doggy age
Create a class Dog with class attribute age_factor equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method human_age which returns the dog’s age in human equivalent.
"""


class Dog:
    age_factor = 7

    def __init__(self, name: str, age: int) -> None:
        self.name = name.title()
        self.age = int(age)

    def human_age(self) -> str:
        result = Dog.age_factor * self.age
        return f"{self.name} will have {result} years old in human equivalent!"


chop = Dog("chop", 5)
print(chop.human_age())
