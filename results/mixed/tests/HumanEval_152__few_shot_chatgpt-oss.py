import pytest

# The functions are assumed to live in a module named `solution.py`
# placed in the same directory as this test file.
from solution import is_palindrome, get_max, compare


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
def test_palindrome_basic():
    assert is_palindrome('radar') is True
    assert is_palindrome('hello') is False


def test_palindrome_empty():
    assert is_palindrome('') is True


def test_palindrome_case_sensitive():
    assert is_palindrome('Radar') is False


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("A", True),                     # single character
        ("aa", True),                    # two equal chars
        ("ab", False),                   # two different chars
        ("Able was I ere I saw ElbA", False),  # case‑sensitive long string
        ("madamimadam", True),           # even length palindrome
        ("12321", True),                 # numeric palindrome
        ("12345", False),                # numeric non‑palindrome
        ("😊🚀🚀😊", True),               # unicode emoji palindrome
        ("😊🚀🚀😢", False),              # unicode emoji non‑palindrome
        ("  ", True),                    # spaces only
        (" a ", True),                   # spaces around a single char
        ("a b a", False),                # spaces inside break palindrome
    ],
)
def test_palindrome_various(input_str, expected):
    """Parametrized checks for a variety of strings, including Unicode."""
    assert is_palindrome(input_str) is expected


def test_palindrome_non_string():
    """The function expects a string; other types should raise a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(123)          # int
    with pytest.raises(TypeError):
        is_palindrome(['r', 'a'])   # list


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
def test_max_positive():
    assert get_max([1, 2, 3]) == 3


def test_max_negative():
    assert get_max([-1, -5, -2]) == -1


def test_max_empty():
    assert get_max([]) is None


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([42], 42),                     # single element
        ([5, 5, 5, 5], 5),              # all equal
        ([-10, -20, -30, -5], -5),      # mix of negatives
        ([0, 0, 0], 0),                 # zeros
        ([2**31 - 1, -2**31], 2**31 - 1),  # large ints
        ([True, False, 0, 1], 1),      # bools are ints (True == 1)
        ([3, 1.5, 2.7], 3),             # floats mixed with ints
    ],
)
def test_max_various(arr, expected):
    """Check `get_max` on a range of typical and edge‑case inputs."""
    assert get_max(arr) == expected


def test_max_non_iterable():
    """Passing a non‑iterable should raise a TypeError."""
    with pytest.raises(TypeError):
        get_max(123)          # int is not iterable
    with pytest.raises(TypeError):
        get_max(None)         # None is not iterable


# ----------------------------------------------------------------------
# Tests for `compare`
# ----------------------------------------------------------------------
def test_compare_examples():
    """The examples from the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]


@pytest.mark.parametrize(
    "scores,guesses,expected",
    [
        # all correct
        ([7, 7, 7], [7, 7, 7], [0, 0, 0]),
        # all off by 1
        ([1, 2, 3], [0, 3, 2], [1, 1, 1]),
        # mixture of positive and negative numbers
        ([-5, 0, 5], [-5, 2, -5], [0, 2, 10]),
        # zeros and large numbers
        ([0, 0, 1000], [0, -1000, 1000], [0, 1000, 0]),
        # duplicate values
        ([4, 4, 4], [4, 5, 3], [0, 1, 1]),
    ],
)
def test_compare_various(scores, guesses, expected):
    """Parametrized checks covering a variety of numeric patterns."""
    assert compare(scores, guesses) == expected


def test_compare_mismatched_lengths():
    """The function should raise a ValueError when the two lists differ in length."""
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])          # shorter guesses
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])          # longer guesses


def test_compare_non_iterable_inputs():
    """Non‑iterable arguments must raise a TypeError."""
    with pytest.raises(TypeError):
        compare(123, [1, 2, 3])             # first arg not iterable
    with pytest.raises(TypeError):
        compare([1, 2, 3], "123")           # second arg not iterable


def test_compare_return_type_and_immutability():
    """Ensure the returned object is a new list (not the same reference)."""
    scores = [1, 2, 3]
    guesses = [1, 0, 5]
    result = compare(scores, guesses)
    assert isinstance(result, list)
    # Mutating the result must not affect the original inputs
    result[0] = 999
    assert scores == [1, 2, 3]
    assert guesses == [1, 0, 5]