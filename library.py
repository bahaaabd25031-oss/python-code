class Library:
    def __init__(self ,name):
        self.name = name
        self.books = []

    def add_book(self ,*added_books):
        for book in added_books:
            self.books.append(book)
    
    def borrow_book(self,*borrowed_books):
        for book in borrowed_books:
            if book in self.books:
                print(book) 
                book.is_borrowed = True
                self.books.remove(book)
            else:
                print(f'{book.name} by {book.author} doesn\'t exist in our library\n')

    def return_book(self,*returned_books):
        for book in returned_books:
            if book.is_borrowed:
                self.books.append(book)
                print(f'{book.name} by {book.author} has been returned successfully\n')
                book.is_borrowed = False
            else:
                print('you didn\'t borrow this book from here\n')

    def __str__(self):
        return f'{self.name} and it has : \n{[book.describe() for book in self.books]}\n'
           
class Book:
    def __init__(self ,name ,author, category = 'other'):
        self.name = name
        self.author = author
        self.category = category
        self.is_borrowed = False
    
    def describe(self):
        return f'{self.name} by {self.author} and the category is: {self.category}'
    
    def __str__(self):
        return self.describe() + '\n'
    
house_wisdom = Library('the house of wisdom')

book1 = Book("'the dumb one'",'bahaa','comedy')
book2 = Book("'the matches seller'",'ali','drama')
book3 = Book("'The Story of Civilization'",'Will Durant','history')

house_wisdom.add_book(book1,book2,book3)
house_wisdom.borrow_book(book1,book2,book3)
house_wisdom.return_book(book1,book2,book3)

print(house_wisdom)