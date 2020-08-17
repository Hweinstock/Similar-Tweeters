import utility
from features import get_headers


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
            "same_author": self.determine_author_match
        }

    def top_n_word_comparison(self, n=100):
        """
        TODO: Get rid of nouns since adjective and verb repetition is more likely to reveal a common author.

        Returns:
            a statistic that compares the most common 100 words in the two texts and how common they are in the other text.


        """
        forward = self.text_1.cross_compare_top_n_words(self.text_2, n)
        backward = self.text_2.cross_compare_top_n_words(self.text_1, n)
        return (forward + backward) / 2.0

    def average_word_length_comparison(self):
        """
        TODO: Figure out an intuitive way to normalize the data to be in (0,1)

        Returns:
            a statistic that compares the average word length between the two texts.

        """

        first_max = self.text_1.average_word_length()
        second_max = self.text_2.average_word_length()

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    def top_n_sentence_lengths_comparison(self, n=10):
        """
        Currently not using frequency comparison.
        TODO: Split into two distinct statistics for find a way to combine them into something more significant
        Args:
            n:

        Returns:
            Two statistics, the first being a comparison of the similarity of top sentence lengths,
            the second being a comparison of top sentence length frequency

        """
        text_1_sentence_lengths, text_1_sentence_length_freqs = self.text_1.split_sentence_length_info(n)
        text_2_sentence_lengths, text_2_sentence_length_freqs = self.text_2.split_sentence_length_info(n)

        # self.check_lengths(text_1_sentence_lengths, text_2_sentence_lengths, "sentence length")

        sentence_length_comp = utility.list_similarity(text_1_sentence_lengths, text_2_sentence_lengths)
        # sentence_length_freq_comp = utility.list_similarity(text_1_sentence_length_freqs, text_2_sentence_length_freqs)

        return sentence_length_comp

    def punctuation_comparison(self, n=5):
        forward = self.text_1.cross_compare_top_n_puncs(self.text_2, n)
        backward = self.text_2.cross_compare_top_n_puncs(self.text_1, n)
        return (forward + backward) / 2.0

        # text_1_top_puncs_pairs = self.text_1.indexed_punctuation_set
        # text_1_top_puncs = text_1_top_puncs_pairs.keys()
        #
        # text_1_top_puncs_freqs = list(text_1_top_puncs_pairs.values())
        # text_2_top_puncs_freqs = [self.text_2.indexed_punctuation_set[punc] for punc in text_1_top_puncs]
        #
        # comp = utility.list_similarity(text_1_top_puncs_freqs, text_2_top_puncs_freqs)
        #
        # return comp

    def determine_author_match(self):
        auth_1 = self.text_1.author
        auth_2 = self.text_2.author

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
        first_max = self.text_1.average_sentence_length()
        second_max = self.text_2.average_sentence_length()

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    def top_n_sentence_lengths_average_comparison(self):
        first_max = self.text_1.average_sentence_length(dict(self.text_1.top_n_sentence_lengths(10)))
        second_max = self.text_2.average_sentence_length(dict(self.text_2.top_n_sentence_lengths(10)))

        if first_max > second_max:
            return second_max / first_max
        else:
            return first_max / second_max

    @property
    def report(self):
        features = get_headers()
        output = []
        for feat in features:
            output.append(self.function_mappings[feat]())
        return output

