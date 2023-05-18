"""
Group: App02_Minyue_Group 38
"""


class ReaderOperation:
    """
    Contains all operations related to a reader.
    """

    def add_bookmark(self, book_title, page_no, reader):
        """
        Add specified reader's bookmarked tuple with book title and book page to bookmark_list.

        Args:
            book_title: book's title
            page_no: page number of corresponding book
            reader: corresponding reader object

        Returns:
            A tuple of bookmarked book title and book page.

        #TODO: wait whether print or return confirmation: handle in main with returned tuple:  print())
        """
        if (book_title, page_no) in reader.bookmark_list:
            print("<< Already bookmarked page {} in <{}>. >>".format(page_no, book_title))
        else:
            reader.bookmark_list.append((book_title, page_no))
            #return (book_title, page_no)
            print("<< Bookmarked page {} in <{}>.>>".format(page_no, book_title))

    def delete_bookmark(self, num, reader):
        """
        Delete specified reader's bookmarked tuple with book title and book page from bookmark_list.

        Args:
            num: user-defined index of bookmark list need to be deleted
            reader: reader object

        Returns:
            Corresponding deleted index of bookmark list

        #TODO: Check num starts from 1 not 0
        #TODO: wait whether print or return: handle in main with  print("<<  num Deleted successfully >>")
        """
        if num > len(reader.bookmark_list):
            print("<< List NO. {} is not in your bookmark list. >>".format(num))
        else:
            reader.bookmark_list.pop()
            #return num
            print("<< List NO. {} is deleted successfully >>".format(num))

    def save_favourite_book(self, book_title, reader):
        """
        Save specified reader's favourite book to favourite_book_list.

        Args:
            book_title: book's title
            reader: reader object

        Returns:
            Saved as facvourite book's title.

        #TODO:  wait whether print or return: handle in main with" print()
        """
        if book_title in reader.favourite_book_list:
            print("<< Already saved <{}> as favourite. >>".format(book_title))
        else:
            reader.favourite_book_list.append(book_title)
            #return book_title
            print("<< Saved <{}> as favourite book. >>".format(book_title))

    def delete_favourite_list(self, parameter, reader):
        """
        Delete specified reader's favourite book from favourite_list.

        Args:
            parameter: An integer of favourite book list number, or a string of book title
            reader: reader object

        Returns:
            parameter: An integer of favourite book list number, or a string of book title

        #TODO: Maybe handle negative
        #TODO:  wait whether print or return: handle in main with: print()
        #TODO: check return parameter is int/str in main()
        """
        if type(parameter) == int:
            if parameter > len(reader.favourite_book_list):
                print("<< List NO.{} is not in your favourite list. >>".format(parameter))
            else:
                reader.favourite_book_list.pop(parameter - 1)
                # return parameter
                print("<< List NO.{} is deleted from your favourite list. >>".format(parameter))
        elif type(parameter) == str:
            if parameter in reader.favourite_book_list:
                reader.favourite_book_list.remove(parameter)
                #return parameter
                print("<< Book title: <{}> is deleted from your favourite list. >>".format(parameter))
            else:
                print("<< Book title: <{}> is not in your favourite list. >>".format(parameter))
        else:
            print("<< ERROR >>")

    def show_all_favorite_book(self, reader):
        """
        Show reader's all favourite books.

        Args:
            reader: reader object
        """
        favourite_index = 0
        if len(reader.favourite_book_list) > 0:
            for favourite in reader.favourite_book_list:
                favourite_index += 1
                print(favourite_index, favourite)
        else:
            print("<< You don't have any favourite book yet. >>")

    def show_all_bookmarks(self, reader):
        """
        Show reader's all bookmarks.

        Args:
            reader: reader object
        """
        bookmark_index = 0
        if len(reader.bookmark_list) > 0:
            for bookmark in reader.bookmark_list:
                bookmark_index += 1
                print("{} <{}> page {}.".format(bookmark_index, bookmark[0], bookmark[1]))
        else:
            print("<< You don't have any bookmark yet. >>")
