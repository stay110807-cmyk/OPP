class library:
    def __init__(self):
        self.user = []
        self.book = []

    def add_user(self, user):
        self.user.append(user)

    def add_book(self, book):
        self.book.append(book)

    def show_books(self):
        for book in self.book:
            print(book.show_book_info())

    def borrow_book(self, user, book):
        if book.available == True:
            book.available = False
            print(f"{user.name} pidio prestado: {book.title}")
        else:
            print(f"El libro {book.title} ya esta prestado")

    def return_book(self, book):
        book.available = True
        print(f"El libro {book.title} fue devuelto")