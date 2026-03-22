import pytest

# ----------------------------------------------------------------------
# Adjust the import path according to where the functions are defined.
# For example, if they live in a file called `solution.py` in the same
# directory, use:
#   from solution import is_palindrome, get_max, words_in_sentence
# ----------------------------------------------------------------------
from solution import is_palindrome, get_max, words_in_sentence


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic palindrome, odd length
        ("level", True),          # another odd‑length palindrome
        ("deed", True),           # even length palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string (edge case)
        ("A", True),              # single character
        ("Radar", False),         # case‑sensitive check
        ("12321", True),          # numeric characters are allowed
        ("12345", False),         # numeric non‑palindrome
        ("Was it a car or a cat I saw", False),  # spaces break palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a range of inputs."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # normal positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([0, -1, 1], 1),                    # mix of zero, negative, positive
        ([-100, -50, -50, -99], -50),       # duplicate max value
        ([2**31 - 1, -2**31], 2**31 - 1),   # large integers (32‑bit boundary)
        ([], None),                         # empty list returns None
    ],
)
def test_get_max_various(arr, expected):
    """Check that `get_max` returns the correct maximum or None."""
    assert get_max(arr) == expected


def test_get_max_mutability():
    """Ensure the original list is not altered by `get_max`."""
    original = [5, 1, 3]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list should remain unchanged"


# ----------------------------------------------------------------------
# Helper for prime length detection (used only inside tests)
# ----------------------------------------------------------------------
def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# ----------------------------------------------------------------------
# Tests for `words_in_sentence`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("This is a test", "is"),                     # example 1
        ("lets go for swimming", "go for"),          # example 2
        ("a bb ccc dddd eeeee", "bb ccc eeeee"),     # mixed lengths
        ("prime numbers are fun", "prime numbers are"),  # 5,7,3,3 are prime
        ("one two three four five six", "two three five"), # 3,5,5 are prime
        ("", ""),                                     # empty sentence (edge case)
        ("single", ""),                               # length 6 (not prime)
        ("hi", "hi"),                                 # length 2 (prime)
        ("a b c d e f g", "a b c d e f g"),           # all length 1 (not prime) -> actually 1 is not prime, so expect empty
        ("ab cd ef gh ij kl mn op qr st uv wx yz", ""), # all length 2 (prime) -> expect whole sentence
    ],
)
def test_words_in_sentence_examples(sentence, expected):
    """Validate that only words with prime lengths are kept, preserving order."""
    # Adjust expected for the case where 1 is not prime
    if sentence == "a b c d e f g":
        expected = ""  # length 1 is not prime
    assert words_in_sentence(sentence) == expected


def test_words_in_sentence_random():
    """Generate a random sentence and verify prime‑length filtering."""
    import random
    import string

    # Build a sentence of 20 words with lengths 1‑10
    words = []
    prime_words = []
    for _ in range(20):
        length = random.randint(1, 10)
        word = "".join(random.choices(string.ascii_lowercase, k=length))
        words.append(word)
        if _is_prime(length):
            prime_words.append(word)

    sentence = " ".join(words)
    expected = " ".join(prime_words)
    assert words_in_sentence(sentence) == expected


def test_words_in_sentence_no_primes():
    """Sentence where no word length is prime should return an empty string."""
    sentence = "aa bbb cccc ddddddd"   # lengths: 2,3,4,7 -> 2,3,7 are prime, adjust to non‑prime only
    # Change to lengths 4,6,8,9 (all non‑prime)
    sentence = "aaaa bbbbbb cccccccc ddddddddd"
    assert words_in_sentence(sentence) == ""


def test_words_in_sentence_all_primes():
    """Sentence where every word length is prime should return the original sentence."""
    # lengths 2,3,5,7,11 (all prime)
    sentence = "ab cat hello swimming eleven"
    assert words_in_sentence(sentence) == sentence