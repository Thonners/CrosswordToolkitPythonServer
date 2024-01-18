import json
from pathlib import Path
import re
from itertools import combinations


class CrosswordToolkitDictionary:
    """Word-list dictionary and functions to look up possible words"""

    def __init__(self) -> None:
        self.load_words()

    def sort_letters(self, letters):
        return "".join((sorted(letters)))

    def load_words(self):
        self.words = {}
        self.anagram = {}
        for i in range(1, 16):
            this_script_path = Path(__file__)
            filepath = Path(
                this_script_path.parent, "static", "words", f"{i}-letter-words.json"
            )
            with open(filepath, "r") as file:
                json_words = json.load(file)
                self.words[i] = [word["word"].lower() for word in json_words]
                self.anagram[i] = {}
                for word in self.words[i]:
                    sorted_letters = self.sort_letters(word)
                    if sorted_letters in self.anagram[i]:
                        self.anagram[i][sorted_letters].append(word)
                    else:
                        self.anagram[i][sorted_letters] = [word]


    def get_multiword_anagrams(self, letters:str, word_lengths: list[int] | None = None):
        num_letters = len(letters)
        if word_lengths is None or len(word_lengths) == 0:
            word_lengths = [num_letters]
        else:
            if total_word_letters := sum(word_lengths) != num_letters:
                raise ValueError(f"Total length of words ({total_word_letters}) not equal to the number of available letters ({num_letters})")
            word_lengths = sorted(word_lengths)
        sorted_letters = "".join(sorted(letters))
        combos = self.get_letter_combos(sorted_letters, word_lengths)
        anagrams = []
        for combo in combos:
            is_anagram = True
            word_anagrams = []
            for potential_word in combo:
                word_length = len(potential_word)
                if potential_word in self.anagram[word_length]:
                    word_anagrams.append(tuple(self.anagram[word_length][potential_word]))
                else:
                    is_anagram = False
            if is_anagram:
                anagrams.append(word_anagrams)
        # Loop through to remove any duplicates which can occur there are multiple words of the same length
        sorted_anagrams = tuple(tuple(sorted(ags)) for ags in anagrams)
        return set(sorted_anagrams)



    def get_letter_combos(self, letters :str, word_lengths):
        if len(word_lengths) == 0:
            raise ValueError("Word lengths must contain at least one item. Got []")
        if len(word_lengths) == 1:
            if word_lengths[0] != len(letters):
                raise ValueError(f"Total length of words ({word_lengths[0]}) not equal to the number of available letters ({len(letters)})")
            return letters
        
        word_letter_combos = combinations(letters, word_lengths[0])
        output  = []
        for first_word_letters in word_letter_combos:
            first_word = "".join(first_word_letters)
            remaining_letters = letters
            for letter in first_word_letters:
                remaining_letters = remaining_letters.replace(letter,"",1)
            remaining_words = word_lengths[1:]
            output.append((first_word, self.get_letter_combos(remaining_letters, remaining_words)))
        return tuple(set(output))
    
    def get_anagrams(self, letters:str):
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
