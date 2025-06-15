class Book:    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status
    
    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self) -> bool:
        return not self._is_checked_out
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    
    def __init__(self):
        self._books = []  # Private list to store books
    
    def add_book(self, book: Book):
        self._books.append(book)
    
    def check_out_book(self, title: str) -> bool:
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title: str) -> bool:
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books currently available.")
            return
        
        print("Available books:")
        for book in available_books:
            print(f"  {book}")