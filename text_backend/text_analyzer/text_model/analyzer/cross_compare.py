from ..utility import utility

# TODO: Generalize these functions


def cross_compare_top_n_words(text_a, text_b):
    """

    Args:
        text_a: dict(TextObject)
        text_b: dict(TextObject)

    Returns:
        The difference in how similar the top n word frequencies in self are from their frequencies in target text.
    """

    source_top_n_word_pairs = text_a["top_w_words"]
    source_top_n_words_freqs = [pair[1] for pair in source_top_n_word_pairs]
    source_top_n_words = [pair[0] for pair in source_top_n_word_pairs]

    target_top_n_words_freqs = []
    for word in source_top_n_words:
        if word in text_b["indexed_word_set"]:
            target_top_n_words_freqs += [text_b["indexed_word_set"][word]]
        else:
            target_top_n_words_freqs += [0]

    frequencies_similarity = utility.list_similarity(source_top_n_words_freqs, target_top_n_words_freqs)

    return frequencies_similarity


def cross_compare_top_n_puncs(text_a, text_b):
    """

    Args:
        text_a: dict(TextObject)
        text_b: dict(TextObject)

    Returns:
        The difference in most common punc usage.
    """

    source_top_n_puncs_pairs = text_a["top_p_puncs"]
    source_top_n_puncs_freqs = [pair[1] for pair in source_top_n_puncs_pairs]
    source_top_n_puncs = [pair[0] for pair in source_top_n_puncs_pairs]

    target_top_n_puncs_freqs = []
    for punc in source_top_n_puncs:
        if punc in text_b["indexed_punc_set"]:
            target_top_n_puncs_freqs += [text_b["indexed_punc_set"][punc]]
        else:
            target_top_n_puncs_freqs += [0]

    frequencies_similarity = utility.list_similarity(source_top_n_puncs_freqs, target_top_n_puncs_freqs)

    return frequencies_similarity
