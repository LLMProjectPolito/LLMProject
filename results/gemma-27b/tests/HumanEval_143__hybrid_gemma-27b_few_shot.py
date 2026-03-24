
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

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_words_in_sentence_example1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_primes():
    assert words_in_sentence("one two four five") == ""

def test_words_in_sentence_all_primes():
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb ccc"

def test_words_in_sentence_mixed():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

def test_words_in_sentence_single_prime():
    assert words_in_sentence("hello") == ""

def test_words_in_sentence_long_sentence():
    sentence = "This is a very long sentence with some words of different lengths"
    assert words_in_sentence(sentence) == "This is a long"

def test_words_in_sentence_repeated_words():
    assert words_in_sentence("a a a") == "a a a"

def test_words_in_sentence_prime_at_start_and_end():
    assert words_in_sentence("a long sentence a") == "a a"

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a bb ccc dddd") == "a bb ccc"

def test_words_in_sentence_all_prime():
    assert words_in_sentence("a bb ccc") == "a bb ccc"

def test_words_in_sentence_no_prime():
    assert words_in_sentence("four five six seven") == ""

def test_words_in_sentence_mixed():
    assert words_in_sentence("one two three four five") == "two three five"

def test_words_in_sentence_long_sentence():
    sentence = "the quick brown fox jumps over the lazy dog"
    assert words_in_sentence(sentence) == "the quick fox over dog"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("one") == ""

def test_words_in_sentence_repeated_words():
    assert words_in_sentence("two two two") == "two two two"

def test_words_in_sentence_edge_case_2():
    assert words_in_sentence("a ab abc abcd abcde") == "a ab abc abcde"

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None