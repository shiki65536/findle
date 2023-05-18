"""
Group: App02_Minyue_Group 38
"""
import random
from user import User


class UserOperation:
    """
    Contains all the operations related to a user.
    """
    user_info_path = "./data/result_data/users.txt"
    user_info_list = []

    def load_user_info(self):
        """
        Loads all registered users' information from user_info_path into user_info_list.

        Returns:
            A Boolean. True: Progress completed; False: Progress error.
        """
        try:
            with open(self.user_info_path, "r", encoding='utf-8') as user_file:
                lines = user_file.readlines()
                for line in lines:
                    info_list = line.split(";;;")
                    self.user_info_list.append(
                        User(info_list[0], info_list[1], info_list[2], info_list[3]))
        except:
            return False
        else:
            return True

    def user_registration(self, user_name, user_password, user_role="user"):
        """
        Create an user object and save it in user_info_list

        Args:
            user_name: user's input for user's name.
            user_password: user's input for user's password.
            user_role: user's role. Default: user.

        Returns:
            A Boolean. True: Progress completed; False: Progress error.

        # TODO: Validation for input nothing
        """
        try:
            # create a list of list from a list of object
            user_data_list = [user_info.__str__().split(";;;")
                              for user_info in self.user_info_list]
            user_names = [user_data[1].lower() for user_data in user_data_list]
            # user's name already exist. case-insensitive
            if user_name.lower() in user_names:
                print("<< This name is already registered. >>")
                return False

            # 10 digits as a unique identifier
            # user_id must be string to be formatted
            user_id = str(random.randint(1000000000, 9999999999))
            user_ids = [user_data[0] for user_data in user_data_list]
            # user's id already exist
            while user_id in user_ids:
                user_id = str(random.randint(1000000000, 9999999999))
            self.user_info_list.append(
                User(user_id, user_name, user_password, user_role))
        except:
            print("<< Error happened in registration. >>")
            return False
        else:
            return True

    def user_login(self, user_name, user_password):
        """
        Authenticate user's login attempt.

        Args:
            user_name: user's input for user's name.
            user_password: user's input for user's password

        Returns:
            A Boolean. True: Progress completed; False: Progress error.
        """
        try:
            # create a list of list from a list of object
            user_data_list = [user_info.__str__().split(";;;")
                              for user_info in self.user_info_list]
            # case insensitive
            user_names = [user_data[1].lower() for user_data in user_data_list]
            if user_name.lower() in user_names:
                index = user_names.index(user_name.lower())
                if not user_data_list[index][2] == user_password:
                    print("<< Password is incorrect. >>")
                    return False
            else:
                print("<< No such user name. >>")
                return False
        except:
            print("<< Error happened in login. >>")
            return False
        else:
            return True

    def write_user_info(self):
        """
        Write all users' information provided in user_info_list into the file in user_info_path.

        Returns:
            A Boolean. True: Progress completed; False: Progress error.
        """
        try:
            for user_obj in self.user_info_list:
                user_flag = 0
                with open(self.user_info_path, 'r', encoding='utf-8') as check_f:
                    for line in check_f.readlines():
                        try:
                            if user_obj.__str__().split(";;;")[0] == line.split(';;;')[0]:
                                user_flag = 1
                        except:
                            user_flag = 0
                if user_flag == 0:
                    with open(self.user_info_path, 'a', encoding='utf-8') as write_f:
                        write_f.write(user_obj.__str__() + "\n")
        except:
            print("<< Can't write user file to info path. >>")
            return False
        else:
            return True
