from text import TextObject

if __name__ == "__main__":

    """
    Examples/Testing
    """
    Dracula = TextObject('test_data/dracula.txt')
    MobyDick = TextObject('test_data/moby_dick.txt')
    print("Dracula: ")
    print("Top 10 words: ", Dracula.top_n_words(10))
    print("Average word length: ", Dracula.average_word_length())
    print("")
    print("Moby Dick:")
    print("Top 10 words: ", MobyDick.top_n_words(10))
    print("Average word length: ", MobyDick.average_word_length())
