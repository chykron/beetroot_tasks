"""
Imports practice

Make a directory with 2 modules; make a function in one of them; then import this function in the other module and
use that in your script of choice.
"""

from module1 import greetings


def main():
    name = "oleh"
    message = greetings(name)
    print(message)


print(main)

if __name__ == '__main__':
    main()
