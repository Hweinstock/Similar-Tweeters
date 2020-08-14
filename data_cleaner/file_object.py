from zipfile import ZipFile
import os

class File:

    def __init__(self, path):
        self.path = "../data/pre_data/" + path
        self.temp_dir = '../data/temp_data'
        self.final_dir = '../data/post_data'

        self.unzip_to_dir()

        base = os.path.splitext(path)[0]

        self.path = "../data/temp_data/" + base + '.txt'
        self.read_in_text()

    def unzip_to_dir(self):
        with ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_dir)

    def read_in_text(self):
        """

        Returns:
            the raw text from the entire file, in current examples, this is a string containing the entire book.

        """
        with open(self.path, "r") as text_file:
            first_line = next(text_file).strip().split(" ")

            author = None

            for index, word in enumerate(first_line):
                if word == 'by':
                    author = " ".join(first_line[index+1:])

            if author is None:
                print("Could not find authors name")
                raise ValueError





    def read_in_author(self):
        pass




