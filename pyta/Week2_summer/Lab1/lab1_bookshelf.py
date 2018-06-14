class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return "Book({},{})".format(self.name, self.author)

    def __lt__(self, other):
        if self.name >= other.name:
            return False
        return True

class Bookshelf:
    def __init__(self, max_book):
        self.max = max_book
        self.book_list = []

    def content(self):
        a = sorted(self.book_list)
        return a

    def add_book(self, name, author):
        book = Book(name, author)
        if len(self.book_list) < self.max:
            self.book_list.append(book)
        return book

    def find_book_name(self, name):
        for i in self.book_list:
            if name == i.name:
                self.book_list.remove(i)
                return i

    def find_book_author(self, author):
        author_book = []
        for i in self.book_list:
            if author == i.author:
                author_book.append(i)
        return author_book

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="lab_pyta.txt")



