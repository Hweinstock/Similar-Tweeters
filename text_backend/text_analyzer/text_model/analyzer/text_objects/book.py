from ..text_objects.text import TextObject
from nltk.tokenize import sent_tokenize


class Book(TextObject):
    # TODO: Write this Object and make Textobject Barebone. Waiting to see what discord files look like.

    @property
    def type(self):
        return "book"

    def list_of_sentences(self):
        """

        Returns:
            a list of sentences found in the raw text
        """
        return sent_tokenize(self.text)

