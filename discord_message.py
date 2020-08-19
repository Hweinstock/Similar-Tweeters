from text import TextObject


class DiscordMessage(TextObject):

    @property
    def type(self):
        return "discord"

    def list_of_sentences(self):
        """

        Returns:
            a list of sentences found in the raw text
        """
        return self.text.split("\n")

