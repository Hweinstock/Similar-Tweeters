from text import TextObject
from utility import words_in_sentence

if __name__ == "__main__":

    """
    Examples/Testing
    1-3, 2-4 same authors
    """

    Dracula = TextObject('test_data/dracula_bstoker.txt')
    MobyDick = TextObject('test_data/moby_dick_hmelville.txt')
    Worm = TextObject('test_data/worm_bstoker.txt')
    Bartleby = TextObject('test_data/bartleby_hmelville.txt')
    print(str(Dracula))
    print(Dracula.report())
    print(MobyDick.report())
    print(Worm.report())
    print(Bartleby.report())

    # Old code for debugging average setence length.
    # s = sorted(MobyDick.list_of_sentences(), key=words_in_sentence, reverse=True)
    # for st in s:
    #     print(st)
    #print("List of Sentences: ", MobyDick.top_n_sentence_lengths(10))
