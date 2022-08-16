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
