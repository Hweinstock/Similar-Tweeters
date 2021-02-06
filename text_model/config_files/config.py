from text_model.analyzer.text_objects.discord_message import DiscordMessage
from text_model.analyzer.text_objects.book import Book
from text_model.analyzer.text_objects.tweet import Tweet

"""
Not sure if this is the best way to do it, but wanted a centralized place to tweak variables, this is what I came up with.
"""


def get_text_object(name):
    key = {
        'discord_message': DiscordMessage,
        'book': Book,
        'tweet': Tweet,
    }
    return key[name]


def return_configs():
    return {
        "cluster_size": 250,
        "top_w_words": 50,
        "top_s_sents": 3,
        "top_p_puncs": 3,
        "test_split": 0.2,
        "default_object": Book,
        "exponential_comparison": False,
        "delete_dead_files": True
    }


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
    return get_features() + ["auth1", "auth2"] + get_label()
