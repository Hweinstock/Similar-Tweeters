from zipfile import ZipFile, BadZipFile
from os.path import splitext
import re


def unzip_to_dir(file, final_dir, root_dir):
    try:
        with ZipFile("../"+root_dir+"/zip_files/" + file, 'r') as zip_ref:
            zip_ref.extractall(final_dir)
        return True
    except BadZipFile:
        return False


def prepare_file(name, root_dir):
    final_dir = '../'+root_dir+'/text_files'
    able_to_unzip = unzip_to_dir(name, final_dir, root_dir)

    if not able_to_unzip:
        return None

    name = splitext(name)[0] + '.txt'
    full_path = "../"+root_dir+"/text_files/" + name

    # Read in text file, identify author and trim gutenberg heading.
    try:
        with open(full_path, "r", encoding="ISO-8859-1") as text_file:

            author = identify_author(text_file)
            new_text = find_start_of_text(text_file)
            # Throw out the data with no content and only a title.
            if len(new_text) < 500:
                return None
    except FileNotFoundError:
        return None

    # Reopen file and write out text without gutenberg heading
    with open(full_path, "w") as text_file:
        text_file.write(new_text)
    full_path = switch_path_for_analyze(full_path)
    return [full_path, author]


def identify_author(text_file):

    current_author = None

    line_num = 0
    while line_num < 200:
        line = next(text_file).strip().split(" ")

        for index, word in enumerate(line):
            if word.lower() == 'by' and line[0][0] != '*':
                new_author = line[index + 1:]

                if current_author is None or len(new_author) > len(current_author):
                    current_author = new_author
                    if len(current_author) >= 2:
                        line_num = 200
                        break

        line_num += 1

    return " ".join(current_author)


def find_start_of_text(text_file):

    while True:
        try:
            next_line = next(text_file).strip()
        except StopIteration:
            return ""
        if re.match('(.*\*END\*)', next_line) is not None or re.match('\*\*\* START', next_line) is not None:
            new_text = text_file.read()
            break

    if new_text is None:
        print("Could not find end of comments/start of book")
        raise ValueError

    return new_text


def switch_path_for_analyze(path):
    return path[3:]
