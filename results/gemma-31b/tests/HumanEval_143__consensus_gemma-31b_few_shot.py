
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

@pytest.mark.parametrize("sentence, expected", [
    # Examples from proposals
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    
    # No prime lengths
    ("a test", ""),
    ("four five", ""),
    ("a best here", ""),
    ("a b c d", ""),
    ("banana", ""),
    ("a e i o u", ""),
    
    # All prime lengths
    ("go for apple", "go for apple"),
    ("he ate apple", "he ate apple"),
    ("hi there", "hi there"),
    ("to the beach tonight", "to the beach tonight"),
    ("abc def ghi", "abc def ghi"),
    ("abc de fghij klmno", "abc de fghij klmno"),
    
    # Mixed lengths
    ("hi you are cool", "hi you are"),
    ("I am a student", "am student"),
    ("I love coding in python", "in"),
    ("i am a", "am"),
    ("to the beach running professional", "to the beach running"),
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"),
    ("abracadabra is magic", "abracadabra is magic"),
    
    # Single word cases
    ("a", ""),
    ("is", "is"),
    ("the", "the"),
    ("test", ""),
    ("apple", "apple"),
    ("hello", "hello"),
    ("at", "at"),
])
def test_words_in_sentence_parametrized(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_prime_boundaries():
    # a(1)X, is(2)Y, the(3)Y, test(4)X, hello(5)Y, school(6)X, seventh(7)Y, eight(5)Y, nine(4)X, ten(3)Y, professional(12)X
    sentence = "a is the test hello school seventh eight nine ten professional"
    expected = "is the hello seventh eight ten"
    assert words_in_sentence(sentence) == expected

def test_max_constraint_length():
    # 99 is not prime (9 * 11)
    assert words_in_sentence("a" * 99) == ""
    # 97 is prime
    assert words_in_sentence("a" * 97) == "a" * 97

def test_empty_and_whitespace():
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""