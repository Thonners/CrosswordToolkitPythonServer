import os
import json
from pathlib import Path
import re


class CrosswordToolkitDictionary:
    """Word-list dictionary and functions to look up possible words"""

    def __init__(self) -> None:
        self.load_words()

    def sort_letters(self, letters):
        return "".join((sorted(letters)))

    def load_words(self):
        self.words = {}
        self.anagram = {}
        for i in range(2, 16):
            this_script_path = Path(__file__)
            filepath = Path(
                this_script_path.parent, "static", "words", f"{i}-letter-words.json"
            )
            with open(filepath, "r") as file:
                json_words = json.load(file)
                self.words[i] = [word["word"] for word in json_words]
                self.anagram[i] = {}
                for word in self.words[i]:
                    sorted_letters = self.sort_letters(word)
                    if sorted_letters in self.anagram[i]:
                        self.anagram[i][sorted_letters].append(word)
                    else:
                        self.anagram[i][sorted_letters] = [word]

    def get_anagrams(self, letters):
        try:
            return self.anagram[len(letters)][self.sort_letters(letters)]
        except KeyError:
            return []

    def get_word_fit(self, letters):
        r = re.compile(letters)
        try:
            return list(filter(r.match, self.words[len(letters)]))
        except KeyError:
            return []
