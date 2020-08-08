from text import TextObject
from utility import words_in_sentence

if __name__ == "__main__":

    """
    Examples/Testing
    """
    Dracula = TextObject('test_data/dracula.txt')
    MobyDick = TextObject('test_data/moby_dick.txt')
    print("Dracula: ")
    print("Top 10 words: ", Dracula.top_n_words(10))
    print("Average word length: ", Dracula.average_word_length())
    print("List of Sentences: ", Dracula.top_n_sentence_lengths(10))
    print("")
    print("Moby Dick:")
    print("Top 10 words: ", MobyDick.top_n_words(10))
    print("Average word length: ", MobyDick.average_word_length())

    # s = sorted(MobyDick.list_of_sentences(), key=words_in_sentence, reverse=True)
    # for st in s:
    #     print(st)
    print("List of Sentences: ", MobyDick.top_n_sentence_lengths(10))
