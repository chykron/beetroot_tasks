"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def squared_and_divided(a: int | float, b: int | float) -> float:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return (a ** 2) / b

    except ValueError:
        print("Invalid input")

    except ZeroDivisionError:
        print("Division by zero can't be performed")


result = squared_and_divided()
print(result)
