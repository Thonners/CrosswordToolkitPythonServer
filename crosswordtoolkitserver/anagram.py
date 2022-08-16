class AnagramSolver:
    def __init__(self) -> None:
        pass

    def get_remaining_letters(self, letters: str, letters_to_be_removed: str) -> str:
        other_letters = letters
        for letter in letters_to_be_removed:
            other_letters = other_letters.replace(letter, "", 1)
        return other_letters

    def get_letter_combos(self, letters: str, length_of_word: int) -> str:
        for i in range(len(letters) - length_of_word + 1):
            if length_of_word > 1:
                # Until we're on the final letter, iterate recursively over the remaining letters and their combos
                for remaining_letters in self.get_letter_combos(
                    letters[i + 1 :], length_of_word - 1
                ):
                    # Yield this letter plus all the combos of the remaining letters
                    yield letters[i] + remaining_letters
            else:
                # If there's only 1 letter in the word, just return the letter!
                yield letters[i]

    def get_all_possible_words(self, letters: str, lengths: list[int]) -> list[str]:
        if sum(lengths) != len(letters):
            raise ValueError(
                f"Mismatch between number of letters ({len(letters)}) and length of requested answers: {lengths}"
            )
        for first_word in self.get_letter_combos(letters, lengths[0]):
            other_letters = self.get_remaining_letters(letters, first_word)
            if len(lengths) == 2:
                yield [first_word, other_letters]
            elif len(lengths) > 2:
                for other_words in self.get_all_possible_words(
                    other_letters, lengths[1:]
                ):
                    yield [first_word, *other_words]

    def get_possible_words_no_repeats(
        self, letters: str, lengths: list[int]
    ) -> list[str]:
        all_possible_words = self.get_all_possible_words(letters, lengths)
        word_sets = []
        for word_set in all_possible_words:
            sorted_words = sorted(word_set)
            if sorted_words not in word_sets:
                word_sets.append(sorted_words)
        return word_sets
