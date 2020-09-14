# Composition is an alternative way of using other class as we are using through inheritance

# Has a relationship
from typing import List


class Book:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Book name {self.name}."

class BookShelf:

    def __init__(self, *books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf has total {len(self.books)} books"





book1 = Book("Book1")
book2 = Book("Book2")
bookShelf = BookShelf(book1, book2)
print(bookShelf)