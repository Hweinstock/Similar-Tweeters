import re

"""
Bunch of helper functions that don't have a place. 
"""


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
