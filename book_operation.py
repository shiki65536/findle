from book import Book
import re
import os


class BookOperation:
    """
    Contains methods for Book Operation
    1. Extracting all the book information like author, title, etc.
    2. Loading all the book information in a dictionary.
    3. Getting chapters, words and lines count for a specific book.
    4. Displaying all the titles of available books.
    5. Showing the chapters of a given book.
    6. Showing content/text for a given book.
    7. Displaying all the books for given author name.
    8. Getting counts for books released in different time periods.
    """

    book_folder_path = "./data/books_data/"
    book_info_path = "./data/result_data/books.txt"
    book_title_list = []
    book_info_dict = {}

    def extract_book_info(self):
        """
        Extracts all book information related to title, author,
        release date, last updated date, producer & language for a given book
        and writes it to a file.

        Returns:
            boolean: returns True is successfully executed, else False
        """
        try:
            # pg10.txt, 16328-0.txt has no author
            for book in os.listdir(self.book_folder_path):
                if (".txt" not in book):
                    continue
                author = None
                release_date = None
                language = None
                producer = None
                last_update_date = None
                with open(self.book_folder_path + book.strip(), 'r', encoding='utf-8') as f:
                    book_content = f.read()
                try:
                    # for 2 lines
                    title = re.search(r'Title: (.*)Author:',
                                      book_content, re.DOTALL).group(1)
                    title = re.sub("[\n ]+", " ", title.strip())
                except:
                    # for 1 line
                    title = re.search(r'Title: (.*)\n', book_content).group(1)
                try:
                    author = re.search(r'Author: (.*)\n',
                                       book_content).group(1)
                except:
                    pass
                try:
                    release_date = re.search(
                        r'Release Date: (.*)\n', book_content).group(1)
                except:
                    pass
                try:
                    last_update_date = re.search(
                        r'(Most recently updated: |Last updated: )(.*)\n', book_content).group(2).replace(']', '')
                except:
                    pass
                try:
                    producer = re.search(
                        r'Produced by[:]? (.*)\n', book_content).group(1)
                except:
                    pass
                try:
                    language = re.search(
                        r'Language: (.*)\n', book_content).group(1)
                except:
                    pass
                if title in self.book_info_dict.keys():
                    continue
                else:
                    self.book_info_dict[title] = Book(title, author, release_date,
                                                               last_update_date, language, producer,
                                                               self.book_folder_path + book)
                if title not in self.book_title_list:
                    self.book_title_list.append(title)
                book_flag = 0
                with open(self.book_info_path, 'r', encoding='utf-8') as check_f:
                    for line in check_f.readlines():
                        try:
                            if title in line.split(';;;')[0]:
                                book_flag = 1
                        except:
                            book_flag = 0
                if book_flag == 0:
                    with open(self.book_info_path, 'a', encoding='utf-8') as write_f:
                        write_f.write(
                            f"{title};;;{author};;;{release_date};;;{last_update_date};;;{language};;;{producer};;;{book}"+"\n")

            return True
        except:
            return False


    def load_book_info(self):
        """
        Loads book related information from book_info_path to 
        book_info_dict and book_title_list.

        Returns:
            Boolean: Returns True is successfully executed, else false.
        """
        try:
            with open(self.book_info_path, 'r', encoding='utf-8') as f:
                book_info = f.readlines()
            for book in book_info:
                book_details = book.split(';;;')
                title = book_details[0]
                if title not in self.book_title_list and title != '\n':
                    self.book_title_list.append(title)
                if title not in self.book_info_dict.keys() and title != '\n':
                    book_obj = Book(title, book_details[1], book_details[2], book_details[3],
                                    book_details[4], book_details[5], book_details[6])
                    self.book_info_dict[title] = book_obj
            return True
        except:
            return False

    def get_counts(self, book_title):
        """
        Gets the count for number of words, lines and chapters 
        of a given book title.

        Args:
            book_title (str): given book title

        Returns:
            tuple: (no_of_chapters, no_of_words, no_of_lines)
        """
        try:
            book_path = self.book_info_dict[book_title].book_path
            book_path = book_path.strip()
            with open(book_path, 'r', encoding='utf-8-sig') as f:
                book_lines = f.readlines()
                f.seek(0)
                book_content = f.read()
            start_index = [idx for idx, s in enumerate(
                book_lines) if "*** START OF" in s][0]
            end_index = [idx for idx, s in enumerate(
                book_lines) if "*** END OF" in s][0]
            relevant_content = book_lines[start_index+1:end_index]
            # no of lines
            no_of_lines = len(relevant_content)
            # no of words
            no_punctuation = ' '.join(relevant_content) #this line is wrong
            for line in relevant_content:
                no_punctuation += line
            no_punctuation = no_punctuation.replace('—', ' ')
            no_punctuation = no_punctuation.replace('-', ' ')
            unwanted_punctuation = ['"', '\'', '*', ':', ',', '.', ',', '’',
                                    '‘', '”', '“', '_', '_', '(', ')', '!', ';', '?', '[', ']']
            for punct in unwanted_punctuation:
                no_punctuation = no_punctuation.replace(punct, '')
            split_words = no_punctuation.split(' ')
            relevant_words = [
                word for word in split_words if word not in ['', '\n']]
            no_of_words = len(relevant_words)
            # no of chapters
            try:
                chapters = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{3}',
                                     book_content, re.IGNORECASE | re.DOTALL).group(1)
                no_of_chapters = len(
                    [chapter for chapter in chapters.split('\n') if len(chapter) > 0])
            except:
                no_of_chapters = 0
            return (no_of_chapters, no_of_words, no_of_lines)
        except:
            try:
                book_path = self.book_folder_path + self.book_info_dict[book_title].book_path
                book_path = book_path.strip()
                with open(book_path, 'r', encoding='utf-8-sig') as f:
                    book_lines = f.readlines()
                    f.seek(0)
                    book_content = f.read()
                start_index = [idx for idx, s in enumerate(
                    book_lines) if "*** START OF" in s][0]
                end_index = [idx for idx, s in enumerate(
                    book_lines) if "*** END OF" in s][0]
                relevant_content = book_lines[start_index+1:end_index]
                # no of lines
                no_of_lines = len(relevant_content)
                # no of words
                no_punctuation = ' '.join(relevant_content) #duplicate
                for line in relevant_content:
                    no_punctuation += line
                no_punctuation = no_punctuation.replace('—', ' ')
                no_punctuation = no_punctuation.replace('-', ' ')
                unwanted_punctuation = ['"', '\'', '*', ':', ',', '.', ',', '’',
                                        '‘', '”', '“', '_', '_', '(', ')', '!', ';', '?', '[', ']']
                for punct in unwanted_punctuation:
                    no_punctuation = no_punctuation.replace(punct, '')
                split_words = no_punctuation.split(' ')
                relevant_words = [
                    word for word in split_words if word not in ['', '\n']]
                no_of_words = len(relevant_words)
                # no of chapters
                try:
                    chapters = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{3}',
                                         book_content, re.IGNORECASE | re.DOTALL).group(1)
                    no_of_chapters = len(
                        [chapter for chapter in chapters.split('\n') if len(chapter) > 0])
                except:
                    no_of_chapters = 0
                return (no_of_chapters, no_of_words, no_of_lines)
            except:
                print("<< Information about book not found. >>")
                return (0, 0, 0)

    def display_titles(self, page_number):
        """
        Displays all the titles available pagewise.

        Args:
            page_number (int): given the titles on a specific page.
        """
        try:
            if page_number <= round(len(self.book_title_list)/10):
                pagewise_titles = {}
                page_counter = 0
                for i in range(len(self.book_title_list)):
                    if i % 10 == 0:
                        page_counter += 1
                        pagewise_titles[page_counter] = [
                            self.book_title_list[i]]
                    else:
                        pagewise_titles[page_counter].append(
                            self.book_title_list[i])
                print(
                    f"========================== List of Book Titles ==========================", end='\n\n')
                for i in range(len(pagewise_titles[page_number])):
                    if 0 <= i < 10:
                        print(str((page_number-1)*10+i+1)+". " +
                              pagewise_titles[page_number][i])
                print("\n")
                print(f"Current Page: {page_number}", end='\n')
                print(
                    f"Total Pages: {round(len(self.book_title_list)/10)}", end='\n\n')
            else:
                print("<< Choose a lower page number, not enough Titles. >>")
        except:
            print("<< Page number invalid. >>")

    def show_book_content(self, book_title):
        """
        Displays the Chapters of given book title, if available.

        Args:
            book_title (str): Book title chosen by user.
        """
        try:
            book_path = self.book_info_dict[book_title].book_path
            book_path = book_path.strip()
            with open(book_path, 'r', encoding='utf-8') as f:
                book_content = f.read()
            try:
                chapter = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{3}',
                                    book_content, re.IGNORECASE | re.DOTALL).group(1)
                print(f"Title: {book_title}", end='\n')
                print("Contents", end='\n')
                print(chapter)
            except:
                print(f"Title: {book_title}", end='\n')
                print("No Contents", end='\n')
        except:
            try:
                book_path = self.book_folder_path + self.book_info_dict[book_title].book_path
                book_path = book_path.strip()
                with open(book_path, 'r', encoding='utf-8') as f:
                    book_content = f.read()
                try:
                    chapter = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{3}',
                                        book_content, re.IGNORECASE | re.DOTALL).group(1)
                    print(f"Title: {book_title}", end='\n')
                    print("Contents", end='\n')
                    print(chapter)
                except:
                    print(f"Title: {book_title}", end='\n')
                    print("No Contents", end='\n')
            except Exception as e:
                print(e)
                print("<< Invalid Title. >>")

    def show_book_text(self, book_title, page_number):
        """
        Shows the book text pagewise

        Args:
            book_title (str): given book title
            page_number (int): given page of the book

        Raises:
            ValueError: for when page number not in book pages
        """
        try:
            book_path = self.book_info_dict[book_title].book_path
            book_path = book_path.strip()
            with open(book_path, 'r', encoding='utf-8') as f:
                book_content = f.read()
            try:
                start_index = re.search(
                    r'\*\*\* START OF(.+?)\n', book_content).end()
                end_index = re.search(
                    r'\*\*\* END OF(.*)\n', book_content).start()
                chapters_text = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{4}',
                                          book_content, re.IGNORECASE | re.DOTALL)

                if len(chapters_text.group(1)) > 0:
                    start_index = chapters_text.end()
                relevant_content = book_content[start_index+1:end_index]
                relevant_content = relevant_content.split('\n')
                chapters = [chap.strip()
                            for chap in chapters_text.group(1).split('\n') if len(chap) > 0]
                clean_chapters = [chap.lower().replace(
                    'chapter', '').strip() for chap in chapters]
                pagewise_content = []
                page_counter = 0
                page = ''
                chapter = 0
                chapter_no = 0
                for line in relevant_content:
                    page_counter += 1
                    page += line+'\n'
                    if re.match(r'^(chapter|stave)\s[I|V|X|0-9]+', line, re.IGNORECASE) \
                        or re.match(r'[I|V|X|0-9]+[\.|:]\s?$', line, re.IGNORECASE) \
                            or line.lower().strip() in [c.lower() for c in chapters+clean_chapters]:
                        chapter += 1
                    if page_counter % 15 == 0:
                        pagewise_content.append(
                            {'page': page, 'chapter': chapter_no})
                        page = ''
                        chapter_no = chapter
                try:
                    if page_number == 0:
                        raise ValueError
                    if len(chapters) > 0:
                        print(
                            f"============== {book_title} - {chapters[pagewise_content[page_number-1]['chapter']]} ==============", end='\n\n')
                        print(pagewise_content[page_number-1]['page'])
                        print(
                            f"======================== end of page {page_number} ========================")
                    else:
                        print(f"-------- {book_title} --------", end='\n\n')
                        print(pagewise_content[page_number-1]['page'])
                        print(f"-------- end of page {page_number} --------")
                except ValueError:
                    print("<< Book starts from page 1. >>")
                except:
                    print("<< Inavlid Page Number. Try a different page. >>")
            except:
                pass
        except:
            try:
                book_path = self.book_folder_path + self.book_info_dict[book_title].book_path
                book_path = book_path.strip()
                with open(book_path, 'r', encoding='utf-8') as f:
                    book_content = f.read()
                try:
                    start_index = re.search(
                        r'\*\*\* START OF(.+?)\n', book_content).end()
                    end_index = re.search(
                        r'\*\*\* END OF(.*)\n', book_content).start()
                    chapters_text = re.search(r'\n\s*content[s]?\.?((.|\n)+?)\n{4}',
                                              book_content, re.IGNORECASE | re.DOTALL)

                    if len(chapters_text.group(1)) > 0:
                        start_index = chapters_text.end()
                    relevant_content = book_content[start_index + 1:end_index]
                    relevant_content = relevant_content.split('\n')
                    chapters = [chap.strip()
                                for chap in chapters_text.group(1).split('\n') if len(chap) > 0]
                    clean_chapters = [chap.lower().replace(
                        'chapter', '').strip() for chap in chapters]
                    pagewise_content = []
                    page_counter = 0
                    page = ''
                    chapter = 0
                    chapter_no = 0
                    for line in relevant_content:
                        page_counter += 1
                        page += line + '\n'
                        if re.match(r'^(chapter|stave)\s[I|V|X|0-9]+', line, re.IGNORECASE) \
                                or re.match(r'[I|V|X|0-9]+[\.|:]\s?$', line, re.IGNORECASE) \
                                or line.lower().strip() in [c.lower() for c in chapters + clean_chapters]:
                            chapter += 1
                        if page_counter % 15 == 0:
                            pagewise_content.append(
                                {'page': page, 'chapter': chapter_no})
                            page = ''
                            chapter_no = chapter
                    try:
                        if page_number == 0:
                            raise ValueError
                        if len(chapters) > 0:
                            print(
                                f"============== {book_title} - {chapters[pagewise_content[page_number - 1]['chapter']]} ==============",
                                end='\n\n')
                            print(pagewise_content[page_number - 1]['page'])
                            print(
                                f"======================== end of page {page_number} ========================")
                        else:
                            print(f"-------- {book_title} --------", end='\n\n')
                            print(pagewise_content[page_number - 1]['page'])
                            print(f"-------- end of page {page_number} --------")
                    except ValueError:
                        print("<< Book starts from page 1. >>")
                    except:
                        print("<< Inavlid Page Number. Try a different page. >>")
                except:
                    pass
            except Exception as e:
                print(e)
                print("<< Invalid Title. >>")

    def get_book_by_author(self, author_name):
        """
        Get all the book titles by a given author.

        Args:
            author_name (str): given author name.
        """
        try:
            author_books = {}
            for title, book_details in self.book_info_dict.items():
                try:
                    if author_name.lower() in book_details.author.lower():
                        author_books[title] = book_details.author
                # for when author does not exist
                except:
                    continue
            print(
                f"========================  Books by {author_name} ========================", end='\n\n')
            counter = 1
            for title, author in author_books.items():
                print(f"{counter}. {title} - {author}")
                counter += 1
        except AttributeError:
            print("<< No books by Author. >>")
        except:
            print("<< Invalid Author name. >>")

    def get_book_release_year(self):
        """
        Gets all the counts of number of books between year periods.
        """
        year_dict = {"1990": 0, "1990_2000": 0, "2000": 0}
        for book_details in self.book_info_dict.values():
            try:
                release_year = int(re.findall(
                    '(\d{4})', book_details.release_date)[0])
                if release_year < 1990:
                    year_dict['1990'] += 1
                elif 1990 <= release_year <= 2000:
                    year_dict['1990_2000'] += 1
                elif release_year >= 2000:
                    year_dict['2000'] += 1
            except:
                continue
        print(f"========================= Total Number of Books ==========================", end='\n\n')
        print(f"Number of books released before 1990: {year_dict['1990']}")
        print(
            f"Number of books released between 1990 and 2000: {year_dict['1990_2000']}")
        print(
            f"Number of books released after 2000: {year_dict['2000']}", end='\n\n')



# print("------------")
# print(len(self.book_info_dict))