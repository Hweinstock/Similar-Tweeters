from text import TextObject
import os
from comparison import Comparison


if __name__ == "__main__":

    """
    Examples/Testing
    1-3, 2-4 same authors
    """

    Dracula = TextObject('test_data/dracula_bstoker.txt')
    MobyDick = TextObject('test_data/moby_dick_hmelville.txt')
    Worm = TextObject('test_data/worm_bstoker.txt')
    Bartleby = TextObject('test_data/bartleby_hmelville.txt')

    textObjects = []
    for file in os.listdir('test_data'):
        textObjects.append(TextObject('test_data/'+file))

    source = textObjects[1]
    for to in textObjects:
        print(source.filepath, to.filepath, Comparison(source, to).report)

    # print(Comparison(Dracula, MobyDick).punctuation_comparison())
    # print(Comparison(Dracula, Worm).punctuation_comparison())
    # print(Comparison(MobyDick, Bartleby).punctuation_comparison())
    # print(str(MobyDick))

    # Old code for debugging average setence length.
    # s = sorted(MobyDick.list_of_sentences(), key=words_in_sentence, reverse=True)
    # for st in s:
    #     print(st)
    #print("List of Sentences: ", MobyDick.top_n_sentence_lengths(10))
