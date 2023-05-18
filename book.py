class Book:

    def __init__(self, title="", author="", release_date="",
                 last_update_date="", language="", producer="", book_path=""):
        """
        Constructor for Book Class.

        Args:
            title (str, optional): book title. Defaults to "".
            author (str, optional): book author. Defaults to "".
            release_date (str, optional): book release date. Defaults to "".
            last_update_date (str, optional): last date the book was updated. Defaults to "".
            language (str, optional): language the book is written in. Defaults to "".
            producer (str, optional): book producer. Defaults to "".
            book_path (str, optional): book path. Defaults to "".
        """
        self.title = title
        self.author = author
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.language = language
        self.producer = producer
        self.book_path = book_path

    def __str__(self):
        """
        Returns all the attributes of a book as a formatted string.

        Returns:
            formatted book information string.
        """
        return f"{self.title};;;{self.author};;;{self.release_date};;;{self.last_update_date};;;{self.language};;;{self.producer};;;{self.book_path}"
        # return ";;;".join(self.title, self.author, self.release_date,
        #                  self.last_update_date, self.language, self.producer, self.book_path)
