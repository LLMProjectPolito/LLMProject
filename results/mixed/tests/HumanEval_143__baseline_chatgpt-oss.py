import pytest

# Adjust the import path according to where the implementation lives.
# If the function is defined in a file called `words.py` in the same directory,
# the line below works as‑is.  Otherwise replace `words` with the appropriate
# module name (e.g. `solution`).
from words import words_in_sentence


@pytest.mark.parametrize(
    "sentence, expected",
    [
        # Basic examples from the statement
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        # Single word – prime length (2, 3, 5, 7, 11 …)
        ("hi", "hi"),                     # length 2 (prime)
        ("cat", "cat"),                   # length 3 (prime)
        ("hello", "hello"),               # length 5 (prime)
        ("awesome", "awesome"),           # length 7 (prime)
        # Single word – non‑prime length
        ("a", ""),                        # length 1 (not prime)
        ("four", ""),                     # length 4 (not prime)
        ("twelve", ""),                   # length 6 (not prime)
        # Mixed prime / non‑prime lengths
        ("one two three four five six", "one two three five"),
        # All words prime length – order must be preserved
        ("go be at it", "go be at it"),
        # No word with prime length – should return empty string
        ("four six eight", ""),
        # Leading / trailing spaces – function should treat them as delimiters only
        ("  prime  numbers  ", "prime numbers"),
        # Multiple consecutive spaces inside the sentence
        ("a   bb    ccc dddd", "bb ccc"),
        # Upper‑case letters – length calculation is case‑agnostic
        ("UPPER lower MixedCase", "UPPER lower MixedCase"),
        # Maximum allowed length (100 characters).  Build a sentence of 10 words,
        # each of prime length 11 (total 110 chars + 9 spaces = 119 > 100, so we
        # keep it under the limit by using length‑5 words).
        ("apple banana grape lemon mango peach plum kiwi pear lime", 
         "apple grape mango peach plum kiwi pear lime"),
    ],
)
def test_words_in_sentence(sentence: str, expected: str):
    """
    Verify that `words_in_sentence` returns exactly the words whose lengths are
    prime numbers, preserving the original order and spacing rules.
    """
    result = words_in_sentence(sentence)
    assert result == expected


def test_immutability_of_input():
    """
    Ensure the original sentence string is not mutated by the function.
    """
    original = "prime test case"
    copy = original[:]
    _ = words_in_sentence(original)
    assert original == copy, "The input string should remain unchanged"


def test_return_type():
    """
    The function must always return a string, even when the result is empty.
    """
    assert isinstance(words_in_sentence("a b c"), str)
    assert isinstance(words_in_sentence("prime"), str)
    assert isinstance(words_in_sentence(""), str)  # even though constraints forbid empty


def test_performance_on_max_length():
    """
    The implementation should handle the maximum allowed input size quickly.
    """
    # 100‑character sentence: 20 words of length 4 (non‑prime) + 19 spaces = 99 chars,
    # plus one extra character to hit exactly 100.
    sentence = "word " * 19 + "wordx"
    # All words have length 4 (non‑prime) except the last one length 5 (prime)
    expected = "wordx"
    assert words_in_sentence(sentence) == expected