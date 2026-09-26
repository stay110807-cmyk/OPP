from books import book
from users import user 
from library import library

book1 = book("001", "OPP fundamentals", "Jhon Lenon", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")
user1 = user("001", "Toledo Diego", "1108")
library = library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.show_books()
library.borrow_book(user1, book1)
library.borrow_book(user1, book1)
library.return_book(book1)
library.borrow_book(user1, book1)