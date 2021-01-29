from tqdm import tqdm
from zipfile import ZipFile, BadZipFile
from os.path import splitext
import re
import os
import csv
from text_model.config_files.config import return_configs

CONFIGS = return_configs()
ZIPS_DIR = "/raw_zips/"
TEXT_DIR = "/raw_text/"


def unzip_to_dir(file, final_dir, root_dir):
    try:
        with ZipFile(root_dir + ZIPS_DIR + file, 'r') as zip_ref:
            zip_ref.extractall(final_dir)
        return True
    except BadZipFile:
        return False


def prepare_file(name, root_dir, id):
    final_dir = root_dir + TEXT_DIR
    able_to_unzip = unzip_to_dir(name, final_dir, root_dir)

    if not able_to_unzip:
        os.remove(root_dir + ZIPS_DIR + file)
        return None, "Unable to Unzip"

    name = splitext(name)[0] + '.txt'
    full_path = root_dir + TEXT_DIR + name


    # Read in text file, identify author and trim gutenberg heading.
    try:
        with open(full_path, "r", encoding="ISO-8859-1") as text_file:

            author = identify_author(text_file)
            author = "".join(["_" if char == "/" else char for char in author])
            new_text = find_start_of_text(text_file)

            # Throw out the data with no content and only a title.
            if len(new_text) < 500:
                return None, "Insufficient Text"
    except FileNotFoundError:
        return None, "Can't find file"

    # Reopen file and write out text without gutenberg heading
    with open(full_path, 'w') as text_file:
        text_file.write(new_text)

    # Rename file to 'id_authFirst_authLast.txt' format
    current_dir = os.path.join(os.path.dirname(full_path), '')
    file_name = str(id) + '_' + '_'.join(author.split()) + ".txt"
    new_path = os.path.join(current_dir + file_name)
    os.rename(full_path, new_path)

    return new_path, "Success"


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


if __name__ == "__main__":
    root_dir = "../data/book_data"
    zip_files_dir = root_dir + ZIPS_DIR
    text_files_dir = root_dir + TEXT_DIR
    zip_files = os.listdir(zip_files_dir)

    print("Cleaning Data...\n")

    for index, file in tqdm(enumerate(zip_files)):

        current_file, msg = prepare_file(file, root_dir, index)

        if current_file is None:
            print("WARNING", file, "Could not prepare file, Possibly of wrong form. ")

            if CONFIGS["delete_dead_files"]:
                os.remove(os.path.join(zip_files_dir, file))
                print("Deleting File")

    text_files = os.listdir(text_files_dir)

    for sec_file in text_files:
        # Remove non-text files from the text file directory.
        if not sec_file.endswith('.txt'):
            os.remove(os.path.join(text_files_dir, sec_file))
        else:
            # Remove any unlabeled data that made its way through.
            first_char = sec_file[0]
            if not first_char.isnumeric():
                os.remove(os.path.join(text_files_dir, sec_file))


