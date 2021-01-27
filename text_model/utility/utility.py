import re
import numpy as np
from numpy.linalg import norm


"""
Bunch of helper functions that don't have a place. 
"""


def author_from_filename(filename):
    author_name_list = re.split('_|\.txt', filename)[1:]
    author_name = " ".join(author_name_list)
    return author_name


def combine_contractions(tokens):
    new_tokens = []
    for index, token in enumerate(tokens):
        if index < len(tokens) - 1:
            next_token = tokens[index+1]
            if next_token == "n't":
                new_tokens.append(token + next_token)
            elif token != "n't":
                new_tokens.append(token)

    return new_tokens


def scale_indexed_set(indexed_set):
    """

    Converts flat numbers to percentages so that they actually make sense.

    Args:
        indexed_set:

    Returns:
        A new dict with percentages.


    """
    total = sum(indexed_set.values())
    if total == 0:
        return {k: 0 for (k, v) in indexed_set.items()}
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


def is_letter(char):
    """

    Args:
        char:

    Returns:
        True if valid letter, false if not

    """
    matched_char = re.match("[a-zA-z]")

    if matched_char is not None and matched_char == char:
        return True
    else:
        return False


def is_capitalized(char):
    """

    Args:
        char:

    Returns:
        True if capitalized, false if not.

    """
    matched_char = re.match("[A-Z]")
    if matched_char is not None and matched_char == char:
        return True
    else:
        return False


def list_similarity(l1, l2):
    """

    Args:
        l1: Python list of nums
        l2: Python list of nums

    Returns:
        Treats l1 and l2 as two vectors in n-space in order to calculate the cosine
        of the angle between the vectors as a method of comparing/quantifying the difference
        between two vectors.

        Also known as cosine similarity.

    """
    a = np.array(l1)
    b = np.array(l2)
    try:
        cos_sim = np.dot(a, b)/(norm(a)*norm(b))
    except ValueError:
        return None

    return cos_sim


def frequency_class(freq, max_freq):
    """
    https://de.wikipedia.org/wiki/H%C3%A4ufigkeitsklasse (translate to English)

    Args:
        freq:
        max_freq:

    Returns:
        returns the frequency class of a given word, this is a metric used to measure
        the frequency of a certain word in relation to the most frequent word.


    """
    return np.floor(0.5 - np.log(freq / max_freq))
