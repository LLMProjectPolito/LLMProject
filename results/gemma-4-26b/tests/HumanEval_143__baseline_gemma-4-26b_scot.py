
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
    # --- Provided Examples ---
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),

    # --- No Prime-Length Words ---
    # Lengths: 1 (a), 4 (abcd), 6 (abcdef)
    ("a abcd abcdef", ""),
    # Lengths: 1 (a), 4 (abcd), 8 (abcdefgh)
    ("a abcd abcdefgh", ""),
    # Lengths: 4 (test), 4 (test), 4 (test)
    ("test test test", ""),

    # --- All Prime-Length Words ---
    # Lengths: 2 (is), 2 (go), 3 (for), 5 (abcde)
    ("is go for abcde", "is go for abcde"),
    # Lengths: 2 (hi), 2 (to), 3 (cat)
    ("hi to cat", "hi to cat"),
    # Lengths: 2 (ab), 2 (cd), 2 (ef)
    ("ab cd ef", "ab cd ef"),

    # --- Single Word Scenarios ---
    ("a", ""),               # Length 1: Not prime
    ("hi", "hi"),            # Length 2: Prime
    ("abc", "abc"),          # Length 3: Prime
    ("abcd", ""),            # Length 4: Not prime
    ("abcde", "abcde"),      # Length 5: Prime
    ("abcdefghi", ""),       # Length 9: Not prime (composite)
    ("abcdefghijk", "abcdefghijk"), # Length 11: Prime

    # --- Mixed Length & Order Preservation ---
    # a(1), hi(2), abc(3), defg(4), abcde(5) -> hi, abc, abcde
    ("a hi abc defg abcde", "hi abc abcde"),
    # Lengths: 3, 4, 2 -> abc, hi
    ("abc defg hi", "abc hi"),
    # Lengths: 7, 1, 2 -> abcdefg, hi
    ("abcdefg a hi", "abcdefg hi"),
])
def test_words_in_sentence(sentence, expected):
    """
    Tests the words_in_sentence function with a wide variety of inputs including
    provided examples, edge cases for prime/non-prime lengths, single words,
    and order preservation.
    """
    assert words_in_sentence(sentence) == expected

def test_sentence_length_constraint_boundary():
    """
    Verifies behavior with a sentence at the upper boundary of the constraint (100 chars).
    """
    # 25 words of 3 letters + 24 spaces = 99 chars. All lengths (3) are prime.
    long_sentence = "abc " * 24 + "abc"
    assert len(long_sentence) <= 100
    assert words_in_sentence(long_sentence) == long_sentence