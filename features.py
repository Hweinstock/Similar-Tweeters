

def get_all_features():
    f = ["top_n_word_comparison",
         "average_word_length_comparison",
         "top_n_sentence_lengths_comparison",
         "punctuation_comparison"]

    return f


def get_label():
    l = ["same_author"]
    return l


def get_features():
    f = ["top_n_word_comparison",
         "average_word_length_comparison",
         "top_n_sentence_lengths_comparison",
         "punctuation_comparison"]

    return f


def get_headers():
    return get_features() + get_label()
