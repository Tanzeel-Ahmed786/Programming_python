'''Exercise # 5
this code is written on 17 august 2024
this code makes a class library'''
class Library:
    
    books = []
    total_books = 0

    def add_book(self,book):
        self.books.append(book)
        self.total_books += 1
    def all_books(self):
        for book in self.books:
            if book == None:
                continue
            print(book,end="  ")

    def no_of_books(self):
        return self.total_books
    def check(self):
        if len(self.books) == self.total_books:
            print("Program is working well.")
        else:
            print("There is some problem in the program")
    
l1 = Library()
l1.add_book("Physics")
l1.add_book("chemistry")
l1.add_book("maths")
print(l1.all_books())
print(l1.no_of_books())
l1.check()

