import utility
import re


class TextObject:
    """
    This Object Wraps a textfile and gives it easier functionality than working directly with file.
    This could eventually be called a message object, but just to keep general its a text object.
    """

    def __init__(self, filepath, precalc=True):
        self.filepath = filepath
        self.text = self.read_full_text()
        self.words = self.list_of_words()
        self.sentences = self.list_of_sentences()

        if precalc:
            self.indexed_word_set = self.index_words()
            self.indexed_sentence_set = self.index_sentences()
            self.index_punctuation_set = self.index_punctuation()
        self.sentences = self.list_of_sentences()

    def number_of_setences(self):
        return len(self.sentences)

    def number_of_words(self):
        return len(self.list_of_words())

    def read_full_text(self):
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
        # Def going to clean up the RE here. Some nasty formatting in the book made this necessary.
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

        return result

    def index_sentences(self):
        """

        Returns:
            a dictionary of format {sentence length : % of occurences}

        """

        occurrences = {}

        for sentence in self.sentences:
            num_words = utility.words_in_sentence(sentence)
            if num_words in occurrences:
                occurrences[num_words] += 1
            else:
                occurrences[num_words] = 1

        scaled_occurrences = utility.scale_indexed_set(occurrences)

        return scaled_occurrences

    def index_words(self):
        """

        Returns:
            a dictionary of format {word : % of occurrences}

        """
        occurrences = {}

        for word in self.words:
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

        scaled_occurrences = utility.scale_indexed_set(occurrences)

        return scaled_occurrences

    def index_punctuation(self):
        """

        Returns:
            a dictionary of format {punc : % of occurences}

        """

        occurrences = {}
        punctuation = ['.', '!', '?', ',', ':', ';', '-']

        for p in punctuation:
            occurrences[p] = self.text.count(p+' ')

        scaled_occurrences = utility.scale_indexed_set(occurrences)
        return scaled_occurrences

    def classify_word_distribution(self):
        frequency_list = {}
        max_freq = self.top_n_words(1)[0][1]

        for word in self.words:
            freq = self.indexed_word_set[word]
            frequency_list[word] = utility.frequency_class(freq, max_freq)

        return frequency_list

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

    def average_sentence_length(self):
        """

        Returns:
            a floating point value representing average sentence length in words.
        """

        total_length = 0
        total_sentences = 0

        for sentence in self.indexed_sentence_set:
            total_length += sentence * self.indexed_sentence_set[sentence]
            total_sentences += self.indexed_sentence_set[sentence]

        return total_length / total_sentences

    def report(self):
        n = 5
        text_report = {
            "top_words": self.top_n_words(n),
            "word_length": self.average_word_length(),
            "sentence_length": self.average_sentence_length(),
            "top_sentences": self.top_n_sentence_lengths(n),
            "punctuation_percentages": self.index_punctuation().items(),

        }
        return text_report

    def __str__(self):
        """
        Only really useful for debugging.
        Returns:
            A report of major statistics regarding the text.

        """

        ret_string ='\n'
        ret_string += self.filepath + '\n'

        ret_string += "Top 10 words: "
        ret_string += str(self.top_n_words(10)) + '\n'

        ret_string += "Average word length: "
        ret_string += str(self.average_word_length()) + '\n'

        ret_string += "Average sentence length: "
        ret_string += str(self.top_n_sentence_lengths(10)) + '\n'

        ret_string += "Punctuation: "
        ret_string += str(self.index_punctuation()) + '\n'

        ret_string += str(utility.top_n_values_of_dict(self.classify_word_distribution(), 10))
        return ret_string
