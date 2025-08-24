

class Library:
    def __init__(self):
        # contains multiple books and memebers
        # main function that connects to the other class objects
        self.members = {}
        self.books = {}
        self.member_id_counter = 100000

    def add_member(self, name):
        """Add a new member or return existing member"""
        if name in self.members:
            existing_member = self.members[name]
            print(f"Member '{name}' already exists with ID: {existing_member.member_id}")
        else:
            # Create new member with auto-incrementing ID
            new_member = Member(name, self.member_id_counter)
            self.members[name] = new_member
            self.member_id_counter += 1  # Increment for next member
            print(f"New member '{name}' created with ID: {new_member.member_id}")
            existing_member = new_member
        
        return existing_member
    
    def get_member(self, name):
        '''Get Member by Name'''
        return self.members.get(name, None)

    def list_member(self):
        '''List Members and ID'''
        if not self.members:
            print("No Members Registers. ")
            return
        
        print("Library Members:")
        for name, member in self.members.items():
            print(f"- {name} (ID: {member.member_id})")

    def borrow_books(self, books):
        ...
    

class Member:
    def __init__(self, name, member_id):
        # contains books that it borrows
        # max of X books based off what I think later
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 5 # default min
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            print("TOO MANY BOOKS BORROWED...")
            return False
        
        self.borrowed_books.append(book)
        print(f'{self.name} borrowed {self.borrowed_books}')
        return True

    def return_book(self, book):
        """Return a borrowed book"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        else:
            print(f"{self.name} doesn't have '{book.title}' borrowed.")
            return False


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by.name}"
        return f"'{self.title}' by {self.author} - {status}"
    
