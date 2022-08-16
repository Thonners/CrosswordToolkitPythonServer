from ..anagram import get_remaining_letters, get_letter_combos, get_all_possible_words


def test_remaining_letters():
    all_letters = "abcdef"
    assert "def" == get_remaining_letters(all_letters, "abc")
    assert "adef" == get_remaining_letters(all_letters, "bc")
    assert "" == get_remaining_letters(all_letters, "abcdef")
    assert "abc" == get_remaining_letters(all_letters, "def")
    assert "ace" == get_remaining_letters(all_letters, "bdf")


def test_remaining_letters_with_repeats():
    all_letters = "abcdefaaa"
    assert "defaaa" == get_remaining_letters(all_letters, "abc")
    assert "defaa" == get_remaining_letters(all_letters, "abca")
    assert "defa" == get_remaining_letters(all_letters, "aaabc")
    assert "defa" == get_remaining_letters(all_letters, "abcaa")
    assert "abcfaaa" == get_remaining_letters(all_letters, "de")


def test_get_letter_combos_short():
    all_letters = "abc"
    assert ["a", "b", "c"] == list(get_letter_combos(all_letters, 1))
    assert ["ab", "ac", "bc"] == list(get_letter_combos(all_letters, 2))
    assert ["abc"] == list(get_letter_combos(all_letters, 3))


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
    ] == list(get_letter_combos(all_letters, 3))
