"""
Fraction

Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
with appropriate checking and error handling
class Fraction:
    pass
x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)
"""
from math import gcd
from typing import Union


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        else:
            other = Fraction(int(other * self.denominator), self.denominator)
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        else:
            other = Fraction(int(other * self.denominator), self.denominator)
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        else:
            other = Fraction(int(other * self.denominator), self.denominator)
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: Union['Fraction', int, float]) -> 'Fraction':
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        else:
            other = Fraction(int(other * self.denominator), self.denominator)
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other: Union['Fraction', int, float]) -> bool:
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        other = Fraction(int(other * self.denominator), self.denominator)
        return self.numerator == other.numerator and self.denominator == other.denominator


x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y == Fraction(3, 4))