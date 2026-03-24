
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

import pytest
from your_module import words_in_sentence  # Replace your_module
from your_module import is_prime  # Import is_prime

def test_is_prime_small_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_small_non_primes():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_sentence_with_no_prime_length_words():
    assert words_in_sentence("this is a test") == ""

def test_sentence_with_one_prime_length_word():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_multiple_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_sentence_with_all_prime_length_words():
    assert words_in_sentence("a be do go") == "a be do go"

def test_sentence_with_mixed_prime_and_non_prime_length_words():
    assert words_in_sentence("a very long sentence") == "a"  # "a" is the only word with a prime length

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  a be do  ") == "a be do"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("a   be  do") == "a be do"

def test_sentence_with_single_letter_words():
    assert words_in_sentence("a b c d") == "a b c d"

def test_sentence_with_longer_words():
    assert words_in_sentence("This is a very long sentence indeed") == "is a"

def test_sentence_with_numbers_in_words():
    assert words_in_sentence("123 abc 45 def") == "abc def"  # Numbers are treated as non-prime.  Documented behavior.

def test_sentence_with_special_characters():
    assert words_in_sentence("hello! world?") == ""  # Special characters are ignored. Clarified behavior.

def test_sentence_with_prime_length_words_at_beginning_and_end():
    assert words_in_sentence("a long sentence b") == "a b"

def test_sentence_with_prime_length_words_in_middle():
    assert words_in_sentence("a very long b sentence") == "a b"

def test_sentence_with_repeated_prime_length_words():
    assert words_in_sentence("a a a") == "a a a"

def test_sentence_with_repeated_non_prime_length_words():
    assert words_in_sentence("this this this") == ""

def test_single_word_sentence_prime():
    assert words_in_sentence("go") == "go"

def test_single_word_sentence_non_prime():
    assert words_in_sentence("this") == ""

def test_sentence_with_mixed_case():
    assert words_in_sentence("a Be Do Go") == "a Be Do Go"

def test_invalid_input_none():
    with pytest.raises(TypeError):
        words_in_sentence(None)

def test_invalid_input_list():
    with pytest.raises(TypeError):
        words_in_sentence(["a", "b"])

def test_single_character_sentence_non_prime():
    assert words_in_sentence("i") == ""  # Single character sentence with non-prime length

def test_sentence_with_one_word_non_prime():
    assert words_in_sentence("this_is_one_word") == ""

def test_sentence_with_multiple_words_one_prime():
    assert words_in_sentence("a very long this") == "a this"

def test_sentence_with_unicode_characters():
    assert words_in_sentence("你好 世界") == "你好 世界" # Unicode characters

def test_sentence_with_empty_words():
    assert words_in_sentence("a  b c") == "a b c"

def test_very_long_sentence():
    long_sentence = "a " * 100
    assert words_in_sentence(long_sentence) == long_sentence