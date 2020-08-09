from text import TextObject
from utility import words_in_sentence

if __name__ == "__main__":

    """
    Examples/Testing
    """
    Dracula = TextObject('test_data/dracula.txt')
    MobyDick = TextObject('test_data/moby_dick.txt')
    print(Dracula.report())
    print(MobyDick.report())

    # Old code for debugging average setence length.
    # s = sorted(MobyDick.list_of_sentences(), key=words_in_sentence, reverse=True)
    # for st in s:
    #     print(st)
    #print("List of Sentences: ", MobyDick.top_n_sentence_lengths(10))
