import re

"""
Bunch of helper functions that don't have a place. 
"""


def scale_indexed_set(indexed_set):
    """

    Converts flat numbers to percentages so that they actually make sense.

    Args:
        indexed_set:

    Returns:
        A new dict with percentages.


    """
    total = sum(indexed_set.values())
    return {k: v / total for (k, v) in indexed_set.items()}


def top_n_values_of_dict(input_dict, n):
    """

    Args:
        input_dict: an indexed set/dict
        n: cutoff point (int)

    Returns:
        The top n keys of dict based on value of keys.

    """
    result = sorted(input_dict.items(), reverse=True, key=lambda item: item[1])
    return result[:n]


def words_in_sentence(sentence):
    """

    Args:
        sentence:

    Returns:
        Int: The number of words in a given sentence

    """
    spaces_count = 0

    for char in sentence:
        if char == " ":
            spaces_count += 1

    return spaces_count + 1


def newline_to_space(char):
    """

    Helper function to trim_sentence

    Args:
        char:

    Returns:
        a space if input is newline,

    """
    if char == '\n':
        return ' '
    else:
        return char


def trim_sentence(sentence):
    """

    Args:
        sentence:

    Returns:
        a cleaned up sentence without escape characters (currently only does \n)

    """
    if "CHAPTER " in sentence:
        return ""
    return "".join(map(newline_to_space, sentence))


def is_word(word):
    """

    Args:
        word: a string

    Returns:
        Boolean of whether or not it qualifies as a word.

    """
    matched_word = re.match("[A-Za-z0-9\']+", word)

    if matched_word is None or matched_word.string != word:
        # This code is to see which string are not identitied as words.
        # if word != "":
        #     if word[0] == "\“":
        #         pass
        #     print(word)
        return False
    return True
