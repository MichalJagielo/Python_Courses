

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "secret"

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


b1 = Book("Janosik", "Jan Kowalski", 859, 59.99)
b2 = Book("Wiedzmin", "Piotr Nowak", 1244, 99.99)

print(b1.get_price())

print(b2.get_price())
b2.set_discount(0.25)
print(round(b2.get_price(), 2))

print(b2._Book__secret)

print(b1)
print(b1.title)