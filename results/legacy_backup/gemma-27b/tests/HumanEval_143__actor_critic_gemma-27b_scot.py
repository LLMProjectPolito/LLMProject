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
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for char in sentence:
        if not 'a' <= char <= 'z' and not 'A' <= char <= 'Z' and char != ' ':
            raise TypeError("Sentence must contain only letters and spaces.")

    words = sentence.split()  # split() handles multiple spaces correctly
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("four five six seven") == ""

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_single_word_non_prime():
    assert words_in_sentence("four") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  is a go  ") == "is a go"

def test_multiple_spaces_between_words():
    assert words_in_sentence("is  a   go") == "is a go"

def test_long_word():
    long_word = "a" * 1000
    assert words_in_sentence(long_word) == ""

def test_prime_words_at_different_positions():
    assert words_in_sentence("two is four seven") == "two is"

def test_non_letter_characters():
    with pytest.raises(TypeError) as excinfo:
        words_in_sentence("hello 123 world")
    assert str(excinfo.value) == "Sentence must contain only letters and spaces."