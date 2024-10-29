#managing a library system
class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"{self.title} - {self.author}"
class LibraryBook(Books):
    def __init__(self, tittle, author, isbn, copiesavailable):
        super().__init__(tittle, author)
        self.isbn = isbn
        self.copiesavailable = copiesavailable

    def borrow_book(self):
        if self.copiesavailable > 0:
            self.copiesavailable -= 1
            return f"{self.title} borrowed. copies left: {self.copiesavailable}"
        else:
            return f" number of copies available: {self.title} unavailable"
    def return_book(self):
        self.copiesavailable += 1
        return f"{self.title} returned. copies left: {self.copiesavailable}"

book1=LibraryBook("The psychology of money", "Morgan Housel", 978-93-901-166-26-8, 20)
print(book1.display())
print(book1.borrow_book())
print(book1.return_book())