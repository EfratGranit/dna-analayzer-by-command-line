from general_func import allowed, shorten_word
from config import error_char


class DnaSequence:
    def __init__(self, string):
        if not isinstance(string, str) or not allowed(string.strip()):
            print(string)
            raise ValueError(error_char)
        self._string = string

    def get_seq(self):
        return self._string

    def insert(self, ind: int, char: chr):
        if ind < len(self._string):
            self._string = self._string[:ind]+char+self._string[ind+1:]
        else:
            raise IndexError('ind at insert is out of range')

    def __getitem__(self, key: int):
        return self._string[key]

    def __setitem__(self, key, value):
        if not isinstance(value, str) or not allowed(value):
            raise ValueError(error_char)
        self._string = self._string[:key]+value+self._string[key+1:]

    def __str__(self):
        return shorten_word(self._string)

    def __eq__(self, other):
        if self._string == other.get_seq():
            return True
        return False

    def __ne__(self, other):
        if self._string == other.get_seq():
            return False
        return True

    def __len__(self):
        return len(self._string)

    def assignment(self, new):
        if (not isinstance(new, str) and type(new) is not DnaSequence) or not allowed(new):
            raise ValueError(error_char)
        self._string = new

