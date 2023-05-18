"""
Group: App02_Minyue_Group 38
"""


class User:
    """
    Contains all information about a user.
    """
    user_id = ""
    user_name = ""
    user_password = ""
    user_role = ""

    def __init__(self, user_id="1000000000", user_name="", user_password="", user_role="user"):
        """
        Constructor of user object.

        Args:
            user_id: 10 digits unique identifier for user.
            user_name: user's name.
            user_password: user's password.
            user_role: user's role. Default is user.
        """
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def __str__(self):
        """
        Returns all the attributes of a user as a formatted string.

        Returns:
            formatted user information string.
        """
        return "{};;;{};;;{};;;{}".format(self.user_id, self.user_name, self.user_password, self.user_role)

