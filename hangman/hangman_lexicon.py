from random import randrange


class HangmanLexicon():
    def __init__(self, fileLocation="./lexicon.txt"):
        self.words = {}
        with open(fileLocation) as f:
            for i, line in enumerate(f):
                self.words[i] = line.replace('\n', '').strip().upper()

        self.wordCount = len(self.words)

    def _get_word_count(self):
        return self.wordCount

    def get_random_word(self):
        randomIndex = randrange(self._get_word_count())
        return self._get_word(randomIndex)

    def _get_word(self, index):
        if index not in self.words:
            raise IndexError('getWord: Illegal index')
        return self.words[index]
