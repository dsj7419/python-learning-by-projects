class Book:
    """
    Represents a book with attributes to store information about title, author, and availability.
    """
    def __init__(self, title, author, ISBN, publication_year, status='available'):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_year = publication_year
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class User:
    """
    Represents a user with attributes for personal information and methods to borrow and return books.
    """
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == 'available':
            book.status = 'checked out'
            self.borrowed_books.append(book)
            return f"{book.title} has been borrowed."
        return f"{book.title} is not available for borrowing."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.status = 'available'
            self.borrowed_books.remove(book)
            return f"{book.title} has been returned."
        return f"{book.title} was not borrowed."


class Staff(User):
    """
    Represents a staff member, inherits from User and has additional methods to manage books.
    """
    def add_book(self, book, library):
        library.books.append(book)
        return f"{book.title} has been added to the library."

    def remove_book(self, book, library):
        if book in library.books:
            library.books.remove(book)
            return f"{book.title} has been removed from the library."
        return f"{book.title} is not in the library."


class Library:
    """
    Represents the library, managing interactions and data flow between books, users, and staff.
    """
    def __init__(self):
        self.books = []
        self.users = []
        self.staff_members = []

    def register_user(self, user):
        self.users.append(user)
        return f"{user.name} has been registered."

    def register_staff(self, staff):
        self.staff_members.append(staff)
        return f"{staff.name} has been registered as staff."

    def check_book_availability(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower() and book.status == 'available':
                return f"{book.title} is available for borrowing."
        return f"{book_title} is not available."

    def get_user_borrowed_books(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return [str(book) for book in user.borrowed_books]
        return "User not found."

    def get_all_available_books(self):
        available_books = [str(book) for book in self.books if book.status == 'available']
        return available_books if available_books else "No available books."

def main():
    # Create sample data
    library = Library()
    library.books.append(Book("1984", "George Orwell", "12345", 1949))
    library.books.append(Book("To Kill a Mockingbird", "Harper Lee", "67890", 1960))
    
    user1 = User("Alice", "U001")
    library.users.append(user1)

    staff1 = Staff("Bob", "S001")
    library.staff_members.append(staff1)
    
    # Main interaction loop
    while True:
        user_input = input("\nOptions: \n1. Check book availability \n2. Borrow book \n3. Return book \n4. Add book \n5. Quit \nSelect an option: ")
        
        if user_input == "1":
            book_name = input("Enter the name of the book: ")
            print(library.check_book_availability(book_name))
        elif user_input == "2":
            book_name = input("Enter the name of the book: ")
            for book in library.books:
                if book.title.lower() == book_name.lower():
                    print(user1.borrow_book(book))
                    break
            else:
                print("Book not found.")
        elif user_input == "3":
            book_name = input("Enter the name of the book: ")
            for book in user1.borrowed_books:
                if book.title.lower() == book_name.lower():
                    print(user1.return_book(book))
                    break
            else:
                print("Book not found.")
        elif user_input == "4":
            book_name = input("Enter the name of the book: ")
            author_name = input("Enter the author's name: ")
            isbn = input("Enter the ISBN: ")
            pub_year = int(input("Enter the publication year: "))
            new_book = Book(book_name, author_name, isbn, pub_year)
            print(staff1.add_book(new_book, library))
        elif user_input == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()