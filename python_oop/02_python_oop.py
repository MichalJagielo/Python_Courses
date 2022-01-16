
class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("January")
b2 = Book("Catch me if you can")
n1 = Newspaper("Newsweek")
n2 = Newspaper("Washington Post")

print(type(b1))
print(type(n1))

print(type(b1) == type(b2))
print(type(b1) == type(n2))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))