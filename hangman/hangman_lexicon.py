class HangmanLexicon():
    def __init__(self):
        self.words = {
            0 : 'BUOY',
            1 : 'COMPUTER',
            2 : 'CONNOISSEUR',
            3 : 'DEHYDRATE',
            4 : 'FUZZY',
            5 : 'HUBBUB',
            6 : 'KEYHOLE',
            7 : 'QUAGMIRE',
            8 : 'SLITHER',
            9 : 'ZIRCON',
        }
        self.wordCount = len(self.words)
    
    def get_word_count(self):
        return self.wordCount

    def get_word(self, index):
        if index not in self.words:
            raise IndexError('getWord: Illegal index')
        return self.words[index]