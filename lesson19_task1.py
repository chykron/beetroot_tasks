"""
Create your own implementation of a built-in function enumerate, named with_index(), which takes two parameters:
iterable and start, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    index = start
    for value in iterable:
        yield index, value
        index += 1


items = ['a', 'b', 'c', 'd', 'e']
for idx, item in with_index(items):
    print(idx, item)
