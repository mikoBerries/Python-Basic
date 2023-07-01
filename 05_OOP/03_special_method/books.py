# Special /dunder/magic are identified by __something__:

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    # book class implementing special string represantife for this class
    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)
    # when len(Book) python build-in func called then what we want to do?
    def __len__(self):
        return self.pages
    # when del(Book) called to something
    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods (build-in python methods)
print(book)
print(len(book))
del book