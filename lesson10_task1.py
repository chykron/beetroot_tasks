"""
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
"""


def oops():
    raise IndexError('oops')


def oops_oops():
    try:
        oops()
    except IndexError:
        print('oops without an Error')


print(oops_oops())
