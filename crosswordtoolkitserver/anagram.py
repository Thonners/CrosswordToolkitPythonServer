def get_remaining_letters(letters: str, letters_to_be_removed: str) -> str:
    other_letters = letters
    for letter in letters_to_be_removed:
        other_letters = other_letters.replace(letter, "", 1)
    return other_letters


def get_letter_combos(letters: str, length_of_word: int) -> str:
    for i in range(len(letters) - length_of_word + 1):
        if length_of_word > 1:
            # Until we're on the final letter, iterate recursively over the remaining letters and their combos
            for remaining_letters in get_letter_combos(
                letters[i + 1 :], length_of_word - 1
            ):
                # Yield this letter plus all the combos of the remaining letters
                yield letters[i] + l
        else:
            # If there's only 1 letter in the word, just return the letter!
            yield letters[i]


def get_all_possible_words(letters: str, lengths: list[int]) -> list[str]:
    if sum(lengths) != len(letters):
        raise ValueError(
            f"Mismatch between number of letters ({len(letters)}) and length of requested answers: {lengths}"
        )
    for first_word in get_letter_combos(letters, lengths[0]):
        other_letters = get_remaining_letters(letters, first_word)
        if len(lengths) == 2:
            yield [first_word, other_letters]
        elif len(lengths) > 2:
            for other_words in get_letter_combos(other_letters, lengths[1:]):
                yield [first_word, *other_words]
