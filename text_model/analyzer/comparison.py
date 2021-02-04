import math

from text_model.utility import utility
from text_model.config_files.config import get_headers
from text_model.config_files.config import return_configs
from text_model.analyzer.cross_compare import cross_compare_top_n_puncs, cross_compare_top_n_words

CONFIGS = return_configs()


class Comparison:
    # TODO: Normalize all of the data better.

    def __init__(self, t1, t2):
        self.text_1 = t1
        self.text_2 = t2
        self.function_mappings = {
            "top_n_word_comparison": self.top_n_word_comparison,
            "average_word_length_comparison": self.average_word_length_comparison,
            "top_n_sentence_lengths_comparison": self.top_n_sentence_lengths_comparison,
            "punctuation_comparison": self.punctuation_comparison,
            "same_author": self.determine_author_match,
            "auth1": self.get_auth_1,
            "auth2": self.get_auth_2
        }

    def get_auth_1(self):
        return self.text_1["author"]

    def get_auth_2(self):
        return self.text_2["author"]

    def top_n_word_comparison(self):
        """
        TODO: Get rid of nouns since adjective and verb repetition is more likely to reveal a common author.

        Returns:
            a statistic that compares the most common 100 words in the two texts and how common they are in the other text.


        """
        forward = cross_compare_top_n_words(self.text_1, self.text_2)
        backward = cross_compare_top_n_words(self.text_2, self.text_1)

        return (forward + backward) / 2.0

    def average_word_length_comparison(self):
        """
        TODO: Figure out an intuitive way to normalize the data to be in (0,1)

        Returns:
            a statistic that compares the average word length between the two texts.

        """

        first_max = self.text_1["average_word_length"]
        second_max = self.text_2["average_word_length"]

        if first_max == 0.0 or second_max == 0.0:
            return 0.0

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    def top_n_sentence_lengths_comparison(self, n=CONFIGS["top_s_sents"]):
        """
        Currently not using frequency comparison.
        TODO: Split into two distinct statistics, find a way to combine them into something more significant
        Args:
            n:

        Returns:
            Two statistics, the first being a comparison of the similarity of top sentence lengths,
            the second being a comparison of top sentence length frequency

        """
        text_1_sentence_lengths = self.text_1["sentence_lengths"]
        text_1_sentence_length_freq = self.text_1["sentence_length_freq"]

        text_2_sentence_lengths = self.text_2["sentence_lengths"]
        text_2_sentence_length_freq = self.text_2["sentence_length_freq"]


        # self.check_lengths(text_1_sentence_lengths, text_2_sentence_lengths, "sentence length")

        sentence_length_comp = utility.list_similarity(text_1_sentence_lengths, text_2_sentence_lengths)
        # sentence_length_freq_comp = utility.list_similarity(text_1_sentence_length_freqs,
        # text_2_sentence_length_freqs)
        return sentence_length_comp

    def punctuation_comparison(self):

        forward = cross_compare_top_n_puncs(self.text_1, self.text_2)
        backward = cross_compare_top_n_puncs(self.text_2, self.text_1)

        return (forward + backward) / 2.0

    def determine_author_match(self):
        auth_1 = self.get_auth_1()
        auth_2 = self.get_auth_2()

        if auth_1 is None or auth_2 is None:
            return None

        shorter_name = auth_1
        bigger_name = auth_2

        if len(auth_1) > len(auth_2):
            shorter_name = auth_2
            bigger_name = auth_1

        for char in shorter_name:
            if char not in bigger_name:
                return False

        return True

    def average_sentence_length_comparison(self):
        first_max = self.text_1["average_sentence_length"]
        second_max = self.text_2["average_sentence_length"]

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    def top_n_sentence_lengths_average_comparison(self):
        first_max = self.text_1["average_top_n_sent_length"]
        second_max = self.text_2["average_top_n_sent_length"]

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    @property
    def report(self):
        features = get_headers()
        output = []
        for feat in features:
            function = self.function_mappings[feat]
            value = function()
            output.append(value)
        return output

    def __dict__(self):
        rep = {}
        for func_key in self.function_mappings:
            func = self.function_mappings[func_key]
            value = func()
            if value is not None:
                if not isinstance(value, str) and math.isnan(value):
                    value = None

            rep[func_key] = value

        return rep

    def __str__(self):
        return str(self.__dict__())


