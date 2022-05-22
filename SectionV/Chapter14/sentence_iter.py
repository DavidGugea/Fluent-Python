import re
import reprlib

RE_WORD = re.compile("\w+")


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            return StopIteration()

        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence ({0})".format(
            reprlib.repr(self.text)
        )

    def __iter__(self):
        return SentenceIterator(self.words)
