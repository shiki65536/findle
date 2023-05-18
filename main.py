from user import User
from user_operation import UserOperation
from reader import Reader
from reader_operation import ReaderOperation
from book import Book
from book_operation import BookOperation


def menu():  # done, but need redesign
    findle_logo = """
███████ ██ ███    ██ ██████  ██      ███████ 
██      ██ ████   ██ ██   ██ ██      ██      
█████   ██ ██ ██  ██ ██   ██ ██      █████   
██      ██ ██  ██ ██ ██   ██ ██      ██      
██      ██ ██   ████ ██████  ███████ ███████ 
"""
    menu_option = """-----------------------------------------------------------------------
Welcome to Findle! 
-----------------------------------------------------------------------
[1] Register
[2] Login
[0] Quit
"""
    print(findle_logo)
    print(menu_option)
    user_input = input(">> Please select your option: ")
    return user_input


def register_login_menu(mode, user_op_obj):  # almost done
    register_login_greeting = """
-----------------------------------------------------------------------
Findle > Account Page
-----------------------------------------------------------------------"""
    print(register_login_greeting)
    # validation for user input for name and password - cant be nothing
    user_input_name = input(">> 1. Please input your name: ")
    user_input_password = input(">> 2. Please input your password: ")
    if len(user_input_name) == 0:
        print("\n<< User Name cannot be empty. >>")
    if len(user_input_password) == 0:
        print("\n<< User Password cannot be empty. >>")
    #user_op_obj = UserOperation()

    if mode == 1:
        # TODO: user_role?
        result = user_op_obj.user_registration(
            user_input_name, user_input_password)
        return [result, user_input_name]
    elif mode == 2:
        result = user_op_obj.user_login(user_input_name, user_input_password)
        return [result, user_input_name]
    else:
        print("<< ERROR >>")
        return [False, ""]


def findle_menu():  # done, but need redesign
    findle_logo = """
███████ ██ ███    ██ ██████  ██      ███████ 
██      ██ ████   ██ ██   ██ ██      ██      
█████   ██ ██ ██  ██ ██   ██ ██      █████   
██      ██ ██  ██ ██ ██   ██ ██      ██      
██      ██ ██   ████ ██████  ███████ ███████ 
"""
    findle_greeting = """-----------------------------------------------------------------------
Findle > Home Page
-----------------------------------------------------------------------"""
    findle_option = """
[1] Show library
[2] Show favourite
[3] Show bookmarks
[4] Search author
[5] Release date
[0] Log out.
    """
    print(findle_logo)
    print(findle_greeting)
    print(findle_option)
    user_input = input(">> Enter your choice: ")
    return user_input


def title_menu(reader_obj, reader_op_obj, book_op_obj,  page_no=1):  # working
    title_operation = """-----------------------------------------------------------------------
[/]Home          [<]Previous          [BOOK_NO]Check           [>]Next
-----------------------------------------------------------------------"""
    BookOperation.display_titles(BookOperation, page_no)
    print(title_operation)
    while True:
        user_input = input(">> Enter your choice: ")
        if user_input == "/":
            # findle_menu()
            break
        elif user_input == "<":
            title_menu(reader_obj, reader_op_obj, book_op_obj, page_no - 1)
            break
        elif user_input == ">":
            title_menu(reader_obj, reader_op_obj, book_op_obj, page_no + 1)
            break
        elif user_input.isdigit():
            content_menu(int(user_input) - 1, page_no,
                         reader_obj, reader_op_obj, book_op_obj)
            break
        else:
            print("\n<< ERROR Please input value from /, <, >, or digit number. >>")


def content_menu(book_index, title_page, reader_obj, reader_op_obj, book_op_obj):  # done
    content_operation = """
-----------------------------------------------------------------------
[/]Back                   [*]Favourite                        [>]Read
-----------------------------------------------------------------------"""
#    book_op_obj = BookOperation()
    count_info = book_op_obj.get_counts(
        book_op_obj.book_title_list[book_index])

    book_op_obj.show_book_content(book_op_obj.book_title_list[book_index])
    print("\n>> {} chapters, {} words, {} lines are in <{}>.".format(count_info[0], count_info[1], count_info[2],
                                                                     book_op_obj.book_title_list[book_index]))
    print(content_operation)

    while True:
        user_input = input(">> Enter your choice: ")
        if user_input == ">":
            text_menu(book_index, reader_op_obj, reader_obj, book_op_obj)
            break
        elif user_input == "/":
            title_menu(reader_obj, reader_op_obj, book_op_obj, title_page)
            break
        elif user_input == "*":
            reader_op_obj.save_favourite_book(
                book_op_obj.book_title_list[book_index], reader_obj)
        else:
            print("\n<< ERROR Please input value from >, /, or *. >>")


def text_menu(book_index, reader_op_obj, reader_obj, book_op_obj, page_no=1):  # working
    text_operation = """
-----------------------------------------------------------------------
[/]Home  [*]Favourite  [+]Bookmark  [<]Previous  [PAGE_NO]Jump  [>]Next
-----------------------------------------------------------------------"""
    # book_op_obj = BookOperation()
    book_op_obj.show_book_text(
        book_op_obj.book_title_list[book_index], page_no)
    print(text_operation)
    while True:
        user_input = input(">> Enter your choice: ")
        if user_input == "/":
            #title_menu(reader_obj, reader_op_obj)
            break
        elif user_input == "*":
            reader_op_obj.save_favourite_book(
                book_op_obj.book_title_list[book_index], reader_obj)
        elif user_input == "+":
            reader_op_obj.add_bookmark(
                book_op_obj.book_title_list[book_index], page_no, reader_obj)
        elif user_input == "<":
            text_menu(book_index, reader_op_obj, reader_obj, book_op_obj,  page_no - 1)
            break
        elif user_input == ">":
            text_menu(book_index, reader_op_obj, reader_obj, book_op_obj, page_no + 1)
            break
        elif user_input.isdigit():
            text_menu(book_index, reader_op_obj, reader_obj, book_op_obj, int(user_input))
            break
        else:
            print("\n<< ERROR Please input value from /, <, >, +, *, or digit number.  >>")


def search_menu():  # done, but need redesign
    book_op_obj = BookOperation()
    search_greeting = """
-----------------------------------------------------------------------
Findle > Search Page
-----------------------------------------------------------------------"""
    print(search_greeting)
    user_input = input(">> Enter author's name: ")
    book_op_obj.get_book_by_author(user_input)


def favourite_menu(reader_op_obj, reader_obj, book_op_obj, page_no=1):
    favourite_greeting = """
-----------------------------------------------------------------------
Findle > Favourite book Page
-----------------------------------------------------------------------"""
    favourite_operation = """
-----------------------------------------------------------------------
[/] Home           [- BOOK_NO/BOOK_NAME] Delete       [BOOK_NO] Read 
-----------------------------------------------------------------------"""
    # TODO: Need limitation when use "<" (shouldn't be allowed in page 1) and ">" (shoudn't be allowd in page last)
    # TODO: "- 4" -> 4 is the index of the list
    print(favourite_greeting)
    reader_op_obj.show_all_favorite_book(reader_obj)
    print(favourite_operation)
    while True:
        user_input = input(">> Enter your choice: ")
        try:
            if user_input == "/":
                # findle_menu()
                break
            elif user_input.isdigit():
                # book_op_obj = BookOperation()
                book_title = reader_obj.favourite_book_list[int(
                    user_input) - 1]
                book_index = book_op_obj.book_title_list.index(book_title)
                text_menu(book_index, reader_op_obj, reader_obj, book_op_obj)
                break
            # TODO: handle "- integer/string" input, when systems recongnize it, call ReaderOperation.favourite_list(self, parameter, reader)
            elif user_input.split()[0] == '-':
                if user_input.split()[1].isdigit():
                    reader_op_obj.delete_favourite_list(
                        int(user_input.split()[1]), reader_obj)
                    break
                elif user_input.split()[1].isalpha():
                    try:
                        print(reader_obj.favourite_book_list)
                        book_index = reader_obj.favourite_book_list.index(
                            user_input.split()[1])
                        reader_op_obj.delete_favourite_list(
                            book_index, reader_obj)
                    except:
                        print("\n<< Book Name not in favourites. >>")
                    break
                else:
                    print("\n<< Please enter in format 'BOOK_NO/BOOK_NAME Delete'. >>")
                    break
            else:
                print("\n<< ERROR >>")
                break
        except Exception as e:
            print(e)
            print("\n<< Invalid option >>")
            break


def bookmark_menu(reader_op_obj, reader_obj, book_op_obj, page_no=1):  # woring
    bookmark_greeting = """
-----------------------------------------------------------------------
Findle > Bookmark Page
-----------------------------------------------------------------------"""
    bookmark_operation = """-----------------------------------------------------------------------
[/] Home               [- BOOK_NO] Delete               [BOOK_NO] Read        
-----------------------------------------------------------------------"""
    # TODO: Need limitation when use "<" (shouldn't be allowed in page 1) and ">" (shoudn't be allowd in page last)
    print(bookmark_greeting)
    reader_op_obj.show_all_bookmarks(reader_obj)
    print(bookmark_operation)
    while True:
        user_input = input(">> Enter your choice: ")
        try:
            if user_input == "/":
                # findle_menu()
                break
            elif user_input.isdigit():
                # book_op_obj = BookOperation()
                book_title = reader_obj.favourite_book_list[int(
                    user_input) - 1]
                book_index = book_op_obj.book_title_list.index(book_title)
                book_page = 1
                for bookmark in reader_obj.bookmark_list:
                    if bookmark[0] == book_title:
                        book_page = bookmark[1]
                    else:
                        print("<< No such page. >>")
                text_menu(book_index, reader_op_obj, reader_obj, book_op_obj, book_page)
                break
            elif user_input.split()[0] == '-':
                if user_input.split()[1].isdigit():
                    reader_op_obj.delete_bookmark(
                        int(user_input.split()[1]), reader_obj)
                    break
                else:
                    print("\n<< Please enter in format '- BOOK_NO'. >>")
                    break
            else:
                print("\n<< ERROR >>")
        except:
            print("\n<< Inavlid Input >>")
            break


def year_menu():  # done, but need redesign
    year_greeting = """
-----------------------------------------------------------------------
Findle > Release Year Page
-----------------------------------------------------------------------"""
    print(year_greeting)
    book_op_obj = BookOperation()
    book_op_obj.get_book_release_year()


def write_reader_info(reader_obj):
    print(reader_obj.bookmark_list)
    print(reader_obj.favourite_book_list)


def load_favourite_information(user_name, user_file_path):
    try:
        with open(user_file_path, 'r', encoding='utf-8') as f:
            users = f.readlines()
        favourite_book_list = []
        bookmark_list = []
        for user in users:
            if user_name.lower() == user.split(';;;')[1].lower():
                try:
                    favourite_book_list = eval(user.split(';;;')[
                        4])
                    bookmark_list = eval(user.split(';;;')[
                        5])
                except:
                    pass
        return (favourite_book_list, bookmark_list)
    except:
        print(
            "<< User favourites not stored last time. Try re-adding. >>")


def write_reader_file(reader_obj, user_file_path):
    try:
        with open(user_file_path, 'r', encoding='utf-8') as check_f:
            user_text_info = check_f.readlines()

        with open(user_file_path, 'w', encoding='utf-8') as replace_f:
            user_data = ""
            for user_info in user_text_info:
                if reader_obj.user_name == user_info.split(';;;')[1]:
                    user_data += (reader_obj.__str__() + "\n")
                else:
                    user_data += user_info
            replace_f.write(user_data)
    except:
        print(
            "<< User favourites not stored. Try re-adding. >>")
        pass


def main():
    main_flag = True
    user_login = False

    user_name = ""

    book_op_obj = BookOperation()
    book_op_obj.extract_book_info()
    book_op_obj.load_book_info()
    user_op_obj = UserOperation()
    user_op_obj.load_user_info()

    while main_flag:
        menu_input = menu()
        user_obj = None
        reader_obj = None
        reader_op_obj = None

        if menu_input == "1":
            register_login_input = register_login_menu(1, user_op_obj)
            if register_login_input[0]:
                user_name = register_login_input[1]
                user_data_list = [user_info.__str__().split(";;;")
                                  for user_info in user_op_obj.user_info_list]
                user_names = [user_data[1].lower()
                              for user_data in user_data_list]
                if user_name.lower() in user_names:
                    index = user_names.index(user_name.lower())
                    user_obj = User(*user_data_list[index][0:4])
                    reader_obj = Reader(
                        *user_data_list[index][0:3], 'reader', favourite_book_list=[], bookmark_list=[])
                    reader_op_obj = ReaderOperation()
                user_login = True
            else:
                print("\n<< Registeration failed. >>")

        elif menu_input == "2":
            register_login_input = register_login_menu(2, user_op_obj)
            if register_login_input[0]:
                # check user's identification
                user_name = register_login_input[1]
                user_data_list = [user_info.__str__().split(";;;")
                                  for user_info in user_op_obj.user_info_list]
                user_names = [user_data[1].lower()
                              for user_data in user_data_list]
                if user_name.lower() in user_names:
                    index = user_names.index(user_name.lower())
                    if user_obj is None:
                        user_obj = User(*user_data_list[index][0:4])
                    if reader_obj is None and reader_op_obj is None:
                        # favourite info may or may not be there
                        fav_book_list, book_list = load_favourite_information(
                            user_name, user_op_obj.user_info_path)
                        print(fav_book_list, book_list)
                        reader_obj = Reader(
                            *user_data_list[index][0:3], 'reader', favourite_book_list=fav_book_list, bookmark_list=book_list)
                        reader_op_obj = ReaderOperation()
                user_login = True
            else:
                print("\n<< Login failed. >>")
        elif menu_input == "0":
            main_flag = False
        else:
            print("\n<< ERROR Please input value from 1, 2, or 0. >>")

        while user_login:
            findle_input = findle_menu()

            if findle_input == "1":  # display book titles() -> show_book_content() -> show_book_text()
                title_menu(reader_obj, reader_op_obj, book_op_obj)
            elif findle_input == "2":  # show all favorite books
                favourite_menu(reader_op_obj, reader_obj, book_op_obj)
            elif findle_input == "3":  # show all bookmarks
                bookmark_menu(reader_op_obj, reader_obj, book_op_obj)
            elif findle_input == "4":  # search
                search_menu()
            elif findle_input == "5":  # show release year
                year_menu()
            elif findle_input == "0":  # logout
                try:
                    user_op_obj.write_user_info()
                    if reader_obj is not None:
                        # if user_obj.__str__().split(";;;")[3] == 'reader':
                        write_reader_file(
                            reader_obj, user_op_obj.user_info_path)
                except:
                    # reader info storing error
                    pass
                user_login = False
            else:
                print("\n<< ERROR Please input value from 1, 2, 3, 4, 5, or 0. >>")


if __name__ == '__main__':
    main()
