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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a test") == ""

def test_single_prime_length_word():
    assert words_in_sentence("is") == "is"

def test_multiple_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test sentence") == "is a"

def test_all_prime_length_words():
    assert words_in_sentence("prime prime prime") == "prime prime prime"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("This   is  a    test") == "is"

def test_long_sentence_with_prime_words():
    assert words_in_sentence("This is a very long sentence with some prime length words") == "is a"

def test_sentence_with_only_one_word_prime():
    assert words_in_sentence("one") == "one"

def test_sentence_with_only_one_word_non_prime():
    assert words_in_sentence("two") == ""