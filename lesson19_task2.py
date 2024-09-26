"""
Create your own implementation of a built-in function range(), named in_range(), which takes three parameters:
start, end, and optional step. Tips: See the documentation for range() function
"""


def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("Step can't be zero")

    if step > 0:
        current = start
        while current < end:
            yield current
            current += step
    else:
        current = start
        while current > end:
            yield current
            current += step


print(list(in_range(3, 10)))
