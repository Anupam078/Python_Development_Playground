class Books:
    def __init__(self, title, author, isbn):
        self.title = title
        self._author = author
        self.__isbn = isbn

    def _update_author_details(self, new_author):
        self._author = new_author
        return f"Author updated to {self._author}"

    def __get_isbn_number(self):
        return self.__isbn

    

B1= Books("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
