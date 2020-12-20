from utility import utility
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

stop_words = stopwords.words('english')


class TextObject:
    """
    This Object Wraps a textfile and gives it easier functionality than working directly with file.
    This could eventually be called a message object, but just to keep general its a text object.
    """

    def __init__(self, filepath, author=None, precalc=True, include_stopwords=False):
        self.filepath = filepath
        self.author = author
        self.include_stopwords = include_stopwords
        self.text = self.read_full_text()
        self.sentences = self.list_of_sentences()
        self.words = self.list_of_words()

        if precalc:
            self.indexed_word_set = self.index_words()
            self.indexed_sentence_set = self.index_sentences()
            self.indexed_punc_set = self.index_punctuation()

            if self.unique_word_count < 10 or self.unique_sentence_length_count < 10:
                print("WARNING", self.filepath, "Not enough words or sentences to qualify")

    @property
    def number_of_sentences(self):
        return len(self.sentences)

    @property
    def number_of_words(self):
        return len(self.words)

    @property
    def unique_word_count(self):
        return len(self.indexed_word_set)

    @property
    def unique_sentence_length_count(self):
        return len(self.indexed_sentence_set)

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
        # https://machinelearningmastery.com/clean-text-machine-learning-python/#:~:text=3.-,Split%20into%20Words,%E2%80%9D%20%E2%80%9C's%E2%80%9C).
        """

        Returns:
            a list of the meaningful words found in the text

        """
        global stop_words

        tokens = word_tokenize(self.text)
        fixed_tokens = utility.combine_contractions(tokens)
        # Remove Punctuation from all the words
        punc_table = str.maketrans('', '', string.punctuation)
        stripped_words = [word.translate(punc_table) for word in fixed_tokens]

        # Lower case and make sure they only contain a-z characters
        words = [word.lower() for word in stripped_words if word.isalpha()]

        if self.include_stopwords:
            return words
        else:
            meaningful_words = [word for word in words if word not in stop_words]
            return meaningful_words

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
        punctuation = ['.', '!', '?', ',', ':', ';']

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

    def top_n_punctuation(self, n):
        """

        Args:
            n: Cutoff point for ranking

        Returns:
            a list ranking top puncs in form [(punc1, count), (punc2, count2)...(puncn, countn)]

        """

        return utility.top_n_values_of_dict(self.indexed_punc_set, n)

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

        return total_length

    def average_sentence_length(self, input_set=None):
        """

        Returns:
            a floating point value representing average sentence length in words.
        """
        if input_set is None:
            sentence_set = self.indexed_sentence_set
        else:
            sentence_set = input_set

        total_length = 0

        for sentence in sentence_set:
            total_length += sentence * sentence_set[sentence]

        return total_length

    def report(self):
        text_report = {
            "top_words": self.top_n_words(10),
            "word_length": self.average_word_length(),
            "sentence_length": self.average_sentence_length(),
            "top_sentences": self.top_n_sentence_lengths(10),
            "punctuation_percentages": self.index_punctuation().items(),

        }
        return text_report

    def cross_compare_top_n_words(self, text_b, n):
        """

        Args:
            text_b: TextObject

        Returns:
            The difference in how similar the top n word frequencies in self are from their frequencies in target text.
        """

        source_top_n_word_pairs = self.top_n_words(n)
        source_top_n_words_freqs = [pair[1] for pair in source_top_n_word_pairs]
        source_top_n_words = [pair[0] for pair in source_top_n_word_pairs]

        target_top_n_words_freqs = []
        for word in source_top_n_words:
            if word in text_b.indexed_word_set:
                target_top_n_words_freqs += [text_b.indexed_word_set[word]]
            else:
                target_top_n_words_freqs += [0]

        freqs_similarity = utility.list_similarity(source_top_n_words_freqs, target_top_n_words_freqs)

        return freqs_similarity

    def cross_compare_top_n_puncs(self, text_b, n):
        source_top_n_puncs_pairs = self.top_n_punctuation(n)
        source_top_n_puncs_freqs = [pair[1] for pair in source_top_n_puncs_pairs]
        source_top_n_puncs = [pair[0] for pair in source_top_n_puncs_pairs]

        target_top_n_puncs_freqs = []
        for punc in source_top_n_puncs:
            if punc in text_b.indexed_punc_set:
                target_top_n_puncs_freqs += [text_b.indexed_punc_set[punc]]
            else:
                target_top_n_puncs_freqs += [0]

        freqs_similarity = utility.list_similarity(source_top_n_puncs_freqs, target_top_n_puncs_freqs)

        return freqs_similarity

    def split_sentence_length_info(self, n):
        sentence_length_pairs = self.top_n_sentence_lengths(n)
        sentence_lengths = [pair[0] for pair in sentence_length_pairs]
        sentence_length_freq = [pair[1] for pair in sentence_length_pairs]
        return sentence_lengths, sentence_length_freq

    @property
    def valid(self):
        if self.unique_word_count < 10 or self.unique_sentence_length_count < 2:
            return False
        return True

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

        return ret_string


if __name__ == "__main__":
    import pickle

    with open('text_objects.dat', 'rb') as pf:
        text_objects = pickle.load(pf)

    print(text_objects[0].report())