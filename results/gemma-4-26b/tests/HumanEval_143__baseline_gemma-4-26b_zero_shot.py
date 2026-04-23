
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
    # Example cases from problem description
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    
    # Edge cases: Single word
    ("a", ""),             # length 1 (not prime)
    ("at", "at"),          # length 2 (prime)
    ("the", "the"),        # length 3 (prime)
    ("test", ""),          # length 4 (not prime)
    ("seven", "seven"),    # length 5 (prime)
    
    # Edge cases: Multiple words with varying lengths
    ("a b c d", ""),       # all length 1 (not prime)
    ("aa bb cc dd", "aa bb cc dd"), # all length 2 (prime)
    ("abc def ghi", "abc def ghi"), # all length 3 (prime)
    ("abcd efgh ijkl", ""), # all length 4 (not prime)
    ("abcde fghij klmno", "abcde fghij klmno"), # all length 5 (prime)
    
    # Mixed length sentences
    ("is it a test", "is it"), # 2, 2, 1, 4 -> 2, 2
    ("prime words are cool", "prime words are"), # 5, 5, 3, 4 -> 5, 5, 3
    ("no primes here", "no"), # 2, 6, 4 -> 2
    ("abc def ghij", "abc def"), # 3, 3, 4 -> 3, 3
    ("abc def ghijk", "abc def ghijk"), # 3, 3, 5 -> 3, 3, 5
    
    # Long words (testing prime/non-prime up to constraints)
    ("a" * 13, "a" * 13), # 13 is prime
    ("a" * 14, ""),       # 14 is not prime
    ("a" * 17, "a" * 17), # 17 is prime
    ("a" * 19, "a" * 19), # 19 is prime
    ("a" * 20, ""),       # 20 is not prime
])
def test_words_in_sentence(sentence, expected):
    """
    Tests the words_in_sentence function with various sentence structures,
    word lengths (prime and non-prime), and edge cases.
    """
    assert words_in_sentence(sentence) == expected