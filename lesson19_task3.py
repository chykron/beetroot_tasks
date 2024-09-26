"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.data):
            raise StopIteration
        value = self.data[self.current_index]
        self.current_index += 1
        return value

    def __getitem__(self, index):
        if index >= len(self.data):
            raise IndexError('Index out of range')
        return self.data[index]


items = MyIterable([1, 2, 3, 4, 5, 6, 7])
for item in items:
    print(item)

print(items[2])
