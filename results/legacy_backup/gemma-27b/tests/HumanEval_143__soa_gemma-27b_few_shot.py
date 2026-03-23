import pytest

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_primes():
    assert words_in_sentence("one two three four") == ""

def test_words_in_sentence_all_primes():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_words_in_sentence_mixed():
    assert words_in_sentence("a bb ccc dddd") == "a bb"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox over"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("one") == ""

def test_words_in_sentence_repeated_words():
    assert words_in_sentence("two two three three") == "two two three three"

def test_words_in_sentence_with_spaces_at_beginning_and_end():
    assert words_in_sentence("  two three  ") == "two three"