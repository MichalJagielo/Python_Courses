
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # def __init__(self, title, author, pages, price):
        # self.title = title
        # self.author = author   ### @dataclass
        # self.pages = pages
        # self.price = price

    def book_info(self):
        return f"{self.title}, by {self.author}"


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

print(b1.title)
print(b2.author)

####
print(b1)

####
print(b1 == b3)

####
b1.title = "Janosik"
b1.author = "Edek z fabryki kredek"
b1.pages = 897
print(b1.book_info())
print(b1)
print(b2)
print(b3)

