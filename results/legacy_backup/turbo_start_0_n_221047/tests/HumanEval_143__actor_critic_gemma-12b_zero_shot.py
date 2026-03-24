import pytest
from your_module import words_in_sentence  # Replace your_module

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word_prime_length():
    assert words_in_sentence("go") == "go"

def test_single_word_non_prime_length():
    assert words_in_sentence("this") == ""

def test_multiple_words_with_prime_lengths():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_with_mixed_lengths():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_words_non_prime_lengths():
    assert words_in_sentence("this is a very long sentence") == ""

def test_all_words_prime_lengths():
    assert words_in_sentence("go for fun") == "go for fun"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  go for  ") == "go for"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("go   for   fun") == "go for fun"

def test_sentence_with_special_characters_not_allowed():
    with pytest.raises(TypeError):
        words_in_sentence("go! for?")

def test_sentence_with_numbers_not_allowed():
    with pytest.raises(TypeError):
        words_in_sentence("go 1 for")

def test_sentence_with_long_words():
    assert words_in_sentence("This is a verylongword test") == ""

def test_sentence_with_short_words():
    assert words_in_sentence("a b c d") == "a b c d"

def test_sentence_with_prime_and_non_prime_words_at_start_and_end():
    assert words_in_sentence("go this is a test fun") == "go fun"

def test_sentence_with_only_one_prime_length_word():
    assert words_in_sentence("this is a go test") == "go"

def test_sentence_with_same_length_words():
    assert words_in_sentence("go go go") == "go go go"

def test_sentence_with_prime_length_words_and_empty_string():
    assert words_in_sentence("go") == "go"