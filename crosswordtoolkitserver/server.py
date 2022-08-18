from .dictionary import CrosswordToolkitDictionary
from .anagram import AnagramSolver


class CrosswordToolkitServer:
    def __init__(self):
        self.dictionary = CrosswordToolkitDictionary()
        self.anagram_solver = AnagramSolver(self.dictionary)

    def get_anagrams(self, letters, lengths=None):
        return self.anagram_solver.get_anagrams(letters, lengths)

    def get_word_fit(self, letters):
        return self.dictionary.get_word_fit(letters)
