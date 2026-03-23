import pytest

# Import the functions to be tested.
# Adjust the module name (`solution`) to match the actual file where the
# implementations live.
from solution import is_palindrome, get_max, x_or_y


# ----------------------------------------------------------------------
# Tests for ``is_palindrome``
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string – edge case
        ("A", True),              # single character
        ("Able was I ere I saw Elba", False),  # case‑sensitive, spaces included
        ("12321", True),          # numeric palindrome
        ("12345", False),         # numeric non‑palindrome
    ],
)
def test_is_palindrome_basic(input_str, expected):
    """Basic functional tests."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_case_sensitive():
    """Explicit test for case‑sensitivity."""
    assert is_palindrome("Radar") is False
    assert is_palindrome("Radar".lower()) is True


def test_is_palindrome_non_string():
    """The function should raise a TypeError when the argument is not a string."""
    with pytest.raises(TypeError):
        is_palindrome(123)          # int
    with pytest.raises(TypeError):
        is_palindrome(None)         # NoneType
    with pytest.raises(TypeError):
        is_palindrome([1, 2, 1])    # list


# ----------------------------------------------------------------------
# Tests for ``get_max``
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # all positive
        ([-1, -5, -2], -1),                 # all negative
        ([42], 42),                         # single element
        ([0, 0, 0], 0),                     # all zeros
        ([5, 5, 5, 5], 5),                  # duplicates
        ([-10, 0, 10, 20, -20], 20),        # mixed values
        ([2**31 - 1, -2**31], 2**31 - 1),   # large ints
    ],
)
def test_get_max_various(arr, expected):
    """Validate correct maximum for a variety of integer lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return ``None``."""
    assert get_max([]) is None


def test_get_max_none_input():
    """Passing ``None`` should raise a TypeError (cannot iterate)."""
    with pytest.raises(TypeError):
        get_max(None)


def test_get_max_non_int_elements():
    """Even though the type hint is ``list[int]``, ``max`` works with
    comparable types – we verify the behaviour."""
    assert get_max([1.5, 2.3, 0.7]) == 2.3
    assert get_max(["b", "a", "c"]) == "c"


# ----------------------------------------------------------------------
# Tests for ``x_or_y``
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,x,y,expected",
    [
        (2, "prime", "not", "prime"),          # smallest prime
        (3, 10, 20, 10),                       # another prime
        (5, "x", "y", "x"),
        (7, 1, 2, 1),
        (11, "yes", "no", "yes"),
        (13, "a", "b", "a"),
        (4, "x", "y", "y"),                    # composite
        (6, 100, 200, 200),
        (8, "foo", "bar", "bar"),
        (9, "foo", "bar", "bar"),
        (10, "foo", "bar", "bar"),
        (1, "x", "y", "y"),                    # 1 is NOT prime
        (0, "x", "y", "y"),                    # 0 is NOT prime
        (-7, "x", "y", "y"),                   # negative numbers are NOT prime
        (15, "x", "y", "y"),                   # composite
        (21, "x", "y", "y"),
        (101, "prime", "composite", "prime"), # larger prime
        (100, "prime", "composite", "composite"),
    ],
)
def test_x_or_y_basic(n, x, y, expected):
    """Check that the function returns ``x`` for prime ``n`` and ``y`` otherwise."""
    assert x_or_y(n, x, y) == expected


def test_x_or_y_type_errors():
    """The function should raise ``TypeError`` when ``n`` is not an integer."""
    with pytest.raises(TypeError):
        x_or_y(3.14, "x", "y")
    with pytest.raises(TypeError):
        x_or_y("7", "x", "y")
    with pytest.raises(TypeError):
        x_or_y(None, "x", "y")


def test_x_or_y_large_prime():
    """Stress test with a relatively large prime number."""
    large_prime = 104729  # 10000th prime
    assert x_or_y(large_prime, "prime", "not",) == "prime"


def test_x_or_y_non_integer_x_y():
    """``x`` and ``y`` can be any objects; ensure they are returned unchanged."""
    class Dummy:
        def __repr__(self):
            return "<Dummy>"
    dummy_x = Dummy()
    dummy_y = Dummy()
    assert x_or_y(2, dummy_x, dummy_y) is dummy_x   # prime → x
    assert x_or_y(4, dummy_x, dummy_y) is dummy_y   # composite → y