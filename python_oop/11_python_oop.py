
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # def __getattribute__(self, name):
    #     if name == "price":
    #         p = super().__getattribute__("price")
    #         d = super().__getattribute__("_discount")
    #         return p - (p * d)
    #     return super(Book, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise  ValueError("The price must be float")
        return super().__setattr__(name, value)

    def __getattr__(self, name):            ######bez def __getattribute__(self, name):
        return name + " is not here"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

b1.price = 42.15
print(b1)

b2.price = float(45)
print(b2)

print(b1.randommm)