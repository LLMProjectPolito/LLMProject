
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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_single_prime_length_word():
    assert words_in_sentence("is") == "is"

def test_multiple_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == ""

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("hello   world") == ""

def test_long_sentence():
    sentence = "a bb ccc dddd eeeee ffffff ggggggg"
    assert words_in_sentence(sentence) == "bb ccc"

def test_all_words_prime_length():
    sentence = "is it a"
    assert words_in_sentence(sentence) == "is it a"

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_not_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_single_non_prime_word():
    assert words_in_sentence("this") == ""

def test_multiple_words_mixed():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_prime_words():
    assert words_in_sentence("go for") == "go for"

def test_sentence_with_no_prime_words():
    assert words_in_sentence("hello world") == ""

def test_sentence_with_all_prime_words():
    assert words_in_sentence("is a go") == "is a go"

def test_long_sentence():
    assert words_in_sentence("This is a long sentence with some words") == "is a"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This  is   a    test") == "is"

def test_sentence_with_prime_and_non_prime_words_at_edges():
    assert words_in_sentence("is this a go") == "is go"

def test_sentence_with_prime_and_non_prime_words_in_middle():
    assert words_in_sentence("this is a go test") == "is go"

def test_sentence_with_repeated_prime_words():
    assert words_in_sentence("is is is") == "is is is"

def test_sentence_with_repeated_non_prime_words():
    assert words_in_sentence("this this this") == ""

def test_sentence_with_mixed_case_words():
    assert words_in_sentence("Is iS a Go") == "Is iS a Go"

def test_sentence_with_long_prime_word():
    assert words_in_sentence("programming") == "programming"

def test_sentence_with_long_non_prime_word():
    assert words_in_sentence("programming123") == ""

def test_sentence_with_numbers_as_words():
    assert words_in_sentence("1 2 3 4 5") == "2 3 5"

def test_sentence_with_special_characters():
    assert words_in_sentence("hello! world?") == ""