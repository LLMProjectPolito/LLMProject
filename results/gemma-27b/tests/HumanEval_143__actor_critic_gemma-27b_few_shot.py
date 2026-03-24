
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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_basic():
    assert words_in_sentence("This is a test") == "is"

def test_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_all_prime_length_words():
    assert words_in_sentence("it is a") == "it is a"

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_word():
    assert words_in_sentence("two") == "two"

def test_single_non_prime_word():
    assert words_in_sentence("four") == ""

def test_mixed_lengths():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

def test_long_sentence():
    assert words_in_sentence("a very long sentence with some words of prime length") == "very long some"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_multiple_spaces():
    assert words_in_sentence("This  is   a test") == "is a"

def test_large_input():
    sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"
    expected = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert words_in_sentence(sentence) == "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z"

def test_non_letter_characters():
    with pytest.raises(TypeError):  # Or ValueError, depending on desired behavior
        words_in_sentence("hello 123 world!")

def test_numbers_and_punctuation():
    with pytest.raises(TypeError):  # Or ValueError, depending on desired behavior
        words_in_sentence("123 !@# test")

def test_very_long_word():
    long_word = "a" * 1009  # 1009 is a prime number
    assert words_in_sentence(long_word) == long_word