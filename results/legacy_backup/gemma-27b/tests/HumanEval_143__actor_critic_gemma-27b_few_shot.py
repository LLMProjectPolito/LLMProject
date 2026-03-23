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
    If the sentence contains non-letter characters, a ValueError is raised.
    The function uses sentence.split() to handle leading/trailing/multiple spaces,
    effectively collapsing multiple spaces into single spaces between words.
    """
    for char in sentence:
        if not char.isalpha():
            raise ValueError("Sentence contains non-letter characters.")

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_prime_word():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_non_prime_word():
    assert words_in_sentence("one") == ""

def test_words_in_sentence_mixed_lengths():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("a very long sentence with some words of prime length") == "very long some"

def test_words_in_sentence_with_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_words_in_sentence_with_multiple_spaces():
    assert words_in_sentence("This  is   a test") == "is a"

def test_words_in_sentence_with_non_letter_characters():
    with pytest.raises(ValueError):
        words_in_sentence("hello123world!")

def test_words_in_sentence_with_non_letter_characters_2():
    with pytest.raises(ValueError):
        words_in_sentence("hello world!")