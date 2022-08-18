from ..anagram import AnagramSolver
from ..dictionary import CrosswordToolkitDictionary

dictionary = CrosswordToolkitDictionary()
anagram_solver = AnagramSolver(dictionary)


def test_remaining_letters():
    all_letters = "abc"
    assert "bc" == anagram_solver.get_remaining_letters(all_letters, "a")
    all_letters = "abcdef"
    assert "def" == anagram_solver.get_remaining_letters(all_letters, "abc")
    assert "adef" == anagram_solver.get_remaining_letters(all_letters, "bc")
    assert "" == anagram_solver.get_remaining_letters(all_letters, "abcdef")
    assert "abc" == anagram_solver.get_remaining_letters(all_letters, "def")
    assert "ace" == anagram_solver.get_remaining_letters(all_letters, "bdf")


def test_remaining_letters_with_repeats():
    all_letters = "abcdefaaa"
    assert "defaaa" == anagram_solver.get_remaining_letters(all_letters, "abc")
    assert "defaa" == anagram_solver.get_remaining_letters(all_letters, "abca")
    assert "defa" == anagram_solver.get_remaining_letters(all_letters, "aaabc")
    assert "defa" == anagram_solver.get_remaining_letters(all_letters, "abcaa")
    assert "abcfaaa" == anagram_solver.get_remaining_letters(all_letters, "de")
    all_letters = "aaabcdef"
    assert "aadef" == anagram_solver.get_remaining_letters(all_letters, "abc")
    assert "adef" == anagram_solver.get_remaining_letters(all_letters, "abca")
    assert "def" == anagram_solver.get_remaining_letters(all_letters, "aaabc")
    assert "def" == anagram_solver.get_remaining_letters(all_letters, "abcaa")
    assert "aaabcf" == anagram_solver.get_remaining_letters(all_letters, "de")


def test_get_letter_combos_short():
    all_letters = "abc"
    assert ["a", "b", "c"] == list(anagram_solver.get_letter_combos(all_letters, 1))
    assert ["ab", "ac", "bc"] == list(anagram_solver.get_letter_combos(all_letters, 2))
    assert ["abc"] == list(anagram_solver.get_letter_combos(all_letters, 3))


def test_get_letter_combos_longer():
    all_letters = "abcde"
    assert [
        "abc",
        "abd",
        "abe",
        "acd",
        "ace",
        "ade",
        "bcd",
        "bce",
        "bde",
        "cde",
    ] == list(anagram_solver.get_letter_combos(all_letters, 3))


def test_get_all_one_words():
    all_letters = "abc"
    lengths = [3]
    assert [["abc"]] == list(
        anagram_solver.get_all_possible_words(all_letters, lengths)
    )


def test_get_all_two_words():
    all_letters = "abc"
    lengths = [2, 1]
    assert [
        ["ab", "c"],
        ["ac", "b"],
        ["bc", "a"],
    ] == list(anagram_solver.get_all_possible_words(all_letters, lengths))
    # Longer...
    all_letters = "abcdef"
    lengths = [5, 1]
    assert [
        ["abcde", "f"],
        ["abcdf", "e"],
        ["abcef", "d"],
        ["abdef", "c"],
        ["acdef", "b"],
        ["bcdef", "a"],
    ] == list(anagram_solver.get_all_possible_words(all_letters, lengths))


def test_get_all_three_words():
    all_letters = "abc"
    lengths = [1, 1, 1]
    assert [
        ["a", "b", "c"],
        ["a", "c", "b"],
        ["b", "a", "c"],
        ["b", "c", "a"],
        ["c", "a", "b"],
        ["c", "b", "a"],
    ] == list(anagram_solver.get_all_possible_words(all_letters, lengths))


def test_get_words_no_repeats():
    letters = "abc"
    lengths = [1, 1, 1]
    assert [["a", "b", "c"]] == anagram_solver.get_possible_words_no_repeats(
        letters, lengths
    )
    letters = "abcd"
    lengths = [1, 1, 2]
    assert [
        ["a", "b", "cd"],
        ["a", "bd", "c"],
        ["a", "bc", "d"],
        ["ad", "b", "c"],
        ["ac", "b", "d"],
        ["ab", "c", "d"],
    ] == anagram_solver.get_possible_words_no_repeats(letters, lengths)
