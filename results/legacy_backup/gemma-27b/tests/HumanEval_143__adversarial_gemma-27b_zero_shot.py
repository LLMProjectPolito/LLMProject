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
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_single_non_prime_word():
    assert words_in_sentence("a") == ""

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_multiple_prime_words():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_mixed_prime_and_non_prime():
    assert words_in_sentence("one two three four five") == "two three five"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "hello world"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("hello   world") == "hello world"

def test_long_sentence():
    sentence = "This is a very long sentence with some prime and non prime words"
    assert words_in_sentence(sentence) == "This very long some"

def test_all_non_prime_words():
    assert words_in_sentence("one two four six eight") == ""

def test_sentence_with_only_prime_length_words():
    assert words_in_sentence("two three five seven eleven") == "two three five seven eleven"

def test_sentence_with_duplicate_prime_words():
    assert words_in_sentence("two two three three") == "two two three three"

def test_sentence_with_special_characters():
    with pytest.raises(TypeError):
        words_in_sentence("hello! world?")