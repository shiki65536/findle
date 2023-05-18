"""
Group: App02_Minyue_Group 38
"""
from user import User


class Reader(User):
    """
    Contains all the information about a reader.
    """
    favourite_book_list = []
    bookmark_list = []

    def __init__(self, user_id, user_name, user_password, user_role, favourite_book_list=[], bookmark_list=[]):
        """
        Constructor of reader object.

        Args:
            user_id: randomly generated 10 digits user identifier
            user_name: user's name
            user_password: user's password
            user_role: user's role
            favourite_book_list: list of reader's favourite book
            bookmark_list: list of tuples storing bookmarked book title and book page
        """
        super().__init__(user_id, user_name, user_password, user_role)
        self.favourite_book_list = favourite_book_list
        self.bookmark_list = bookmark_list

    def __str__(self):
        """
        Returns all the attributes of a rear as a formatted string.

        Returns:
            formatted reader information string.
        """
        #return super.__str__(self)
        return super().__str__() + ";;;" + str(self.favourite_book_list) + ";;;" + str(self.bookmark_list)

        return "{};;;{};;;{};;;{};;;{};;;{}".format(self.user_id, self.user_name, self.user_password, \
                                                    self.user_role, self.favourite_book_list, self.bookmark_list)

reader = Reader("1234", "ccc", "bbb", "ddd")
user = User("1234", "ccc", "bbb", "ddd")
print(reader)