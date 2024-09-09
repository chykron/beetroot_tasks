"""
Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.
"""


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def __str__(self):
        return f"My name is {self.first_name} {self.last_name}, I'm {self.age} years old"


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, year: str) -> None:
        super().__init__(first_name, last_name, age)
        self.year = str(year)

    def study(self) -> str:
        if self.year == '1':
            self.year += 'st'
        elif self.year == '2':
            self.year += 'nd'
        elif self.year == '3':
            self.year += 'rd'
        else:
            self.year += 'th'
        return f"{super().__str__()}. Currently I'm on the {self.year} year of studying!"


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, age: int, salary: int) -> None:
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def income(self) -> str:
        return f"{super().__str__()} and my salary is {self.salary}$ of yearly income!"


person = Person("John", "Doe", 22)
as_student = Student(person.first_name, person.last_name, person.age, "3")
print(as_student.study())
as_teacher = Teacher("Jane", person.last_name, 43, 35000)
print(as_teacher.income())
