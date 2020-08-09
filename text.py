import utility
import re


class TextObject:
    """
    This Object Wraps a textfile and gives it easier functionality than working directly with file.
    """
    def __init__(self, filepath, precalc=True):
        self.filepath = filepath
        self.text = self.read_full_file()
        if precalc:
            self.indexed_word_set = self.index_words()
            self.indexed_sentence_set = self.index_sentences()
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
        return [word.lower() for word in re.split('\s|,|\.|;|:|\n|--|–|\"|-|—|”|\(|\)|\’', self.text) if utility.is_word(word)]

    def list_of_sentences(self):
        """

        Returns:
            a list of sentences found in the raw text
        """
        result = []
        for sentence in re.split('[\.\!\?]\s', self.text):
            trimmed_sentence = utility.trim_sentence(sentence)
            if trimmed_sentence != "":
                result.append(trimmed_sentence)
        #return [utility.trim_sentence(sentence) for sentence in re.split('[\.\!\?]\s', self.text)]
        return result

    def index_sentences(self):
        sentence_list = self.list_of_sentences()

        occurrences = {}

        for sentence in sentence_list:
            num_words = utility.words_in_sentence(sentence)
            if num_words in occurrences:
                occurrences[num_words] += 1
            else:
                occurrences[num_words] = 1

        return occurrences

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

        return utility.top_n_values_of_dict(self.indexed_word_set, n)

    def top_n_sentence_lengths(self, n):
        """

        Args:
            n: Cutoff point for ranking

        Returns:
            A list ranking top sentence lengths in form [(length1, count), (length2, count2)...(lengthn, countn)]

        """

        return utility.top_n_values_of_dict(self.indexed_sentence_set, n)

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

    def report(self):
        ret_string ='\n'
        ret_string += self.filepath + '\n'

        ret_string += "Top 10 words: "
        ret_string += str(self.top_n_words(10)) + '\n'

        ret_string += "Average word length: "
        ret_string += str(self.average_word_length()) + '\n'

        ret_string += "Average sentence length: "
        ret_string += str(self.top_n_sentence_lengths(10)) + '\n'

        return ret_string
