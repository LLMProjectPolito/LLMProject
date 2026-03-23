import pytest

# The function `words_in_sentence` is assumed to be imported from the module under test.
# from your_module import words_in_sentence


@pytest.mark.parametrize(
    "sentence,expected",
    [
        # Provided examples
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        # Single word cases
        ("hi", "hi"),                     # length 2 (prime)
        ("worlds", ""),                   # length 6 (not prime)
        # Mixed prime / non‑prime lengths
        ("I am ok", "am ok"),             # 1,2,2 → only 2‑letter words kept
        ("a four sixseven eightnine", ""),  # 1,4,8,9 → no prime lengths
        # Leading/trailing whitespace (default split should ignore them)
        ("  hello world  ", "hello world"),
        # Multiple spaces between words
        ("hi   there", "hi there"),
        # All words prime length
        ("we go to be", "we go to be"),   # lengths 2,2,2,2
        # No prime length words with varied lengths
        ("a four sixseven eightnine ten", "ten"),  # only "ten" (3) is prime
        # Maximum length sentence (100 chars)
        (
            "ab cd ef gh ij kl mn op qr st uv wx yz aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz",
            "ab cd ef gh ij kl mn op qr st uv wx yz aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz",
        ),
    ],
)
def test_words_in_sentence(sentence, expected):
    """
    Verify that `words_in_sentence` returns only the words whose lengths are prime numbers,
    preserving the original order and handling whitespace correctly.
    """
    assert words_in_sentence(sentence) == expected


def test_empty_string_returns_empty():
    """
    Although the problem constraints state length >= 1, ensure the function gracefully
    handles an empty input if it occurs.
    """
    assert words_in_sentence("") == ""


def test_non_alpha_characters():
    """
    The specification restricts input to letters only. If other characters appear,
    the function should either ignore them or raise an error. This test checks that
    it does not silently include them in the output.
    """
    # Using a string with a numeric character; expected behavior is to treat the token as a word.
    # If the implementation validates characters, it may raise; we accept either outcome.
    sentence = "hi 123 there"
    result = words_in_sentence(sentence)
    # Only "hi" (len 2) and "there" (len 5) have prime lengths; "123" length 3 is prime but contains digits.
    # The safe expectation is that non‑alphabetic tokens are excluded.
    assert result == "hi there"