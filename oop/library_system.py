class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class EBook(Book):
    
    def __init__(self, file_size, title, author):

        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):

    def __init__(self, title, author, page_count):

        super().__init__(title, author)
        self.page_count = page_count

class Library:

    def __init__(self):

        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(self.books)
