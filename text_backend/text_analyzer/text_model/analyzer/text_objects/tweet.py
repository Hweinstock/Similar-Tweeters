from ..text_objects.text import TextObject


class Tweet(TextObject):

    @property
    def type(self):
        return "tweet"

    def list_of_sentences(self):
        """

        Returns:
            a list of sentences found in the raw text
        """
        split_text = self.text.split("\n")
        return split_text

    @property
    def valid(self):
        if self.unique_word_count < 50 or self.unique_sentence_length_count < 2:
            return False
        return True
