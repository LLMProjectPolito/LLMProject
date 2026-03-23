import pytest

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
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    words = sentence.split()
    result = []
    for word in words:
        if not all('a' <= char <= 'z' for char in word):
            raise ValueError("Sentence contains non-letter characters.")
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_single_non_prime_length_word():
    assert words_in_sentence("aa") == ""

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_prime_and_non_prime():
    assert words_in_sentence("a aa bbb ccc dddd") == "a ccc"

def test_long_sentence():
    sentence = "This is a very long sentence with some words of different lengths"
    assert words_in_sentence(sentence) == "is This long"

def test_sentence_with_only_one_word():
    assert words_in_sentence("hello") == "hello"

def test_prime_word_at_sentence_start():
    assert words_in_sentence("a very long sentence") == "a"

def test_prime_word_at_sentence_end():
    assert words_in_sentence("very long sentence a") == "a"

def test_sentence_with_all_words_length_2():
    assert words_in_sentence("aa bb cc dd") == "aa bb cc dd"

def test_sentence_with_all_words_length_4():
    assert words_in_sentence("aaaa bbbb cccc dddd") == ""

def test_multiple_spaces():
    assert words_in_sentence("  a  bb   ") == "a"

def test_large_prime_length():
    sentence = "a" * 97 + "b"
    assert words_in_sentence(sentence) == ""

def test_constraint_violation():
    with pytest.raises(ValueError):
        words_in_sentence("hello, world!")

def test_sentence_with_mixed_lengths():
    assert words_in_sentence("a bb ccc dddd ee e") == "a bb ccc e"