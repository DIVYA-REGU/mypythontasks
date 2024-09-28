import datetime

class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed_copies = 0

    def borrow(self):
        """Borrow a book copy."""
        if self.borrowed_copies < self.copies:
            self.borrowed_copies += 1
            print(f"Book '{self.title}' borrowed successfully.")
            return True
        print(f"Sorry, all copies of '{self.title}' are currently borrowed.")
        return False

    def return_book(self):
        """Return a borrowed book copy."""
        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1
            print(f"Book '{self.title}' returned successfully.")
            return True
        print(f"No copies of '{self.title}' are currently borrowed.")
        return False

    def is_available(self):
        """Check if the book is available for borrowing."""
        return self.borrowed_copies < self.copies


class Member:
    """Class representing a library member."""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.library_card = LibraryCard(self)

    def borrow_book(self, book):
        """Borrow a book using the library card."""
        if book.borrow():
            self.library_card.borrowed_books.append(book)
            self.library_card.borrowed_dates[book] = datetime.datetime.now()

    def return_book(self, book):
        """Return a borrowed book using the library card."""
        if book in self.library_card.borrowed_books:
            book.return_book()
            self.library_card.borrowed_books.remove(book)
            del self.library_card.borrowed_dates[book]

    def get_borrowed_books(self):
        """Get a list of borrowed books."""
        return self.library_card.borrowed_books


class Librarian:
    """Class representing a librarian."""
    
    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        """Add a book to the library inventory."""
        library.add_book(book)

    def search_book(self, library, title):
        """Search for a book in the library inventory."""
        return library.search_book(title)


class Library:
    """Class representing the library."""
    
    def __init__(self):
        self.inventory = []

    def add_book(self, book):
        """Add a book to the library inventory."""
        self.inventory.append(book)
        print(f"Book '{book.title}' added to the library.")

    def search_book(self, title):
        """Search for a book by title."""
        for book in self.inventory:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found in the library.")
        return None

    def list_books(self):
        """List all books in the library inventory."""
        for book in self.inventory:
            availability = "Available" if book.is_available() else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}")


class LibraryCard:
    """Class representing a library card for members."""
    
    def __init__(self, member):
        self.member = member
        self.borrowed_books = []
        self.borrowed_dates = {}

    def calculate_fines(self):
        """Calculate fines for overdue books."""
        total_fine = 0
        for book, borrow_date in self.borrowed_dates.items():
            overdue_days = (datetime.datetime.now() - borrow_date).days - 14  # Assume 14 days borrowing period
            if overdue_days > 0:
                fine = overdue_days * 1.0  # $1 fine per overdue day
                total_fine += fine
                print(f"Book '{book.title}' is overdue by {overdue_days} days. Fine: ${fine:.2f}")
        return total_fine


# Example usage
if __name__ == "__main__":
    library = Library()
    librarian = Librarian("Alice")

    # Adding books to the library
    librarian.add_book(library, Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3))
    librarian.add_book(library, Book("1984", "George Orwell", "9780451524935", 2))
    librarian.add_book(library, Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1))

    # Listing all books
    print("\nLibrary Inventory:")
    library.list_books()

    # Creating members
    member1 = Member("John Doe", "M001")
    member2 = Member("Jane Smith", "M002")

    # Borrowing books
    print("\nJohn borrowing '1984':")
    member1.borrow_book(library.search_book("1984"))
    print("\nJane borrowing 'The Great Gatsby':")
    member2.borrow_book(library.search_book("The Great Gatsby"))

    # Listing borrowed books
    print("\nJohn's borrowed books:")
    for book in member1.get_borrowed_books():
        print(book.title)

    # Returning books
    print("\nJohn returning '1984':")
    member1.return_book(library.search_book("1984"))

    # Calculating fines
    print("\nCalculating fines for John:")
    total_fine = member1.library_card.calculate_fines()
    print(f"Total fine for {member1.name}: ${total_fine:.2f}")
