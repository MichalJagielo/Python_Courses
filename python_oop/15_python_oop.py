
from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 50))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "Janosik"
    author: str = "Mr Smith"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)