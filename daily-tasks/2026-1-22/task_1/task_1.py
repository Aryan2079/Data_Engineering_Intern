# Task 1: Create a class Book with attributes title and author. Then create two different objects from this class and print their details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Programming with Python", "Aryan Bhattarai")

print(book.title)
print(book.author)