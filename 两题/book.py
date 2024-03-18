class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def print_info(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)


class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        super().__init__(title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes

    def print_info(self):  # method print_info()
        print("Book Information:")
        print("   Book Title:", self.title)
        print("   Author:", self.author)
        print("   Publisher:", self.publisher)
        print("   Publication Date:", self.publication_date)
        print("   Edition:", self.edition)
        print("   Number of Volumes:", self.num_volumes)



if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publication_date = input()

    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_volumes = int(input())

    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()

    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_volumes)
    my_encyclopedia.print_info()
