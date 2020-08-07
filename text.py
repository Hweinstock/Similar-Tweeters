from utility import is_word
import re


class TextObject:
    """
    This Object Wraps a textfile and gives it easier functionality than working directly with file.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.text = self.read_full_file()
        self.indexed_word_set = self.index_words()
        self.sentences = self.list_of_sentences()

    def read_full_file(self):
        """

        Returns:
            the raw text from the entire file, in current examples, this is a string containing the entire book.

        """
        file = open(self.filepath, "r")
        text = file.read()
        file.close()
        return text

    def list_of_words(self):
        """

        Returns:
            a list with words splits based on re-match. This is not perfect, but will be easier with less puncuation (on Discord)

        """
        return [word.lower() for word in re.split('\s|,|\.|;|:|\n|--|–|\"|-|—|”|\(|\)|\’', self.text) if is_word(word)]

    def list_of_sentences(self):
        """

        Returns:
            a list of sentences found in the raw text
        """
        return [sentence for sentence in re.split('\.|\!|\?', self.text)]

    def index_words(self):
        """

        Returns:
            a dictionary of format {word : # of occurrences}

        """
        word_list = self.list_of_words()
        occurrences = {}

        for word in word_list:
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

        return occurrences

    def top_n_words(self, n):
        """

        Args:
            n: Cutoff point for ranking

        Returns:
            A list ranking top words in form [(word, count), (word2, count2)...(wordn, countn)]

        """
        sorted_words = sorted(self.indexed_word_set.items(), reverse=True, key=lambda item: item[1])
        return sorted_words[:n]

    def average_word_length(self):
        """

        Returns:
            A floating point value representing average word length.

        """
        total_length = 0
        total_words = 0

        for word in self.indexed_word_set:
            total_length += len(word) * self.indexed_word_set[word]
            total_words += self.indexed_word_set[word]

        return total_length / total_words


