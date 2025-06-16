books = []

def add_book(title, author):
    books.append({"title":title, "author":author})
    
  
add_book("Brave New World", "Aldous Huxley")
print(books)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    