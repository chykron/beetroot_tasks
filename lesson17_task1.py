"""
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different. For instance, Dog’s can be to print "woof woof",
while Cat’s can be to print "meow".
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def animal_talk(animal: Animal):
    # Generic function that performs the talk method
    animal.talk()


dog = Dog()
cat = Cat()
print(animal_talk(dog))
print(animal_talk(cat))
