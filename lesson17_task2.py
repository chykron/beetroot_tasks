"""
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list
for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
"""


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name={self.name!r}, country={self.country!r}, birthday={self.birthday!r})"

    def __str__(self):
        return f"{self.name} from {self.country} in {self.birthday}"


class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author: 'Author'):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name={self.name!r}, year={self.year!r}, author={self.author!r})"

    def __str__(self):
        return f"{self.name} by {self.author.name} in {self.year}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: 'Author') -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: 'Author') -> list:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name={self.name!r}, books={self.books!r}, authors={self.authors!r})"

    def __str__(self):
        return f"Library: {self.name} with {len(self.books)} books and {len(self.authors)} authors"
