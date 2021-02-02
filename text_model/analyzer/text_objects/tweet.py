from text_model.analyzer.text_objects.text import TextObject


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
