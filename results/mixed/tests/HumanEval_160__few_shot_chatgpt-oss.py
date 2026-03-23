# test_suite.py
import pytest

# Import the functions under test.
# Adjust the import path according to where the implementation lives.
# For example, if the functions are defined in a file named `solution.py`,
# the import would be: from solution import is_palindrome, get_max, do_algebra
from solution import is_palindrome, get_max, do_algebra


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic odd‑length palindrome
        ("level", True),          # another odd‑length palindrome
        ("deed", True),           # even‑length palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string (edge case)
        ("A", True),              # single character
        ("RaceCar", False),       # case‑sensitive check
        ("12321", True),          # numeric characters
        ("123321", True),         # even numeric palindrome
        ("12345", False),         # numeric non‑palindrome
        ("madam im adam", False), # spaces break palindrome (function is literal)
        ("madamimadam", True),    # palindrome without spaces
        ("😀🙃😀", True),          # Unicode characters
        ("😀🙃😎", False),         # Unicode non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # typical positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([], None),                         # empty list returns None
        ([0, 0, 0], 0),                     # all zeros
        ([-10, 0, 10, 20, -20], 20),        # mixed signs
        ([2**31, -2**31, 0], 2**31),        # large integers
        ([5, 5, 5, 5], 5),                  # duplicates
    ],
)
def test_get_max_various(arr, expected):
    assert get_max(arr) == expected


def test_get_max_mutability():
    """Ensure the original list is not modified by `get_max`."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list should remain unchanged"


# ----------------------------------------------------------------------
# Tests for `do_algebra`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "operators,operands,expected",
    [
        # Simple addition and subtraction
        (["+", "-"], [10, 5, 2], 13),               # 10 + 5 - 2 = 13
        # Mixed precedence (multiplication before addition)
        (["+", "*"], [2, 3, 4], 14),                # 2 + 3 * 4 = 14
        # All operators together
        (["+", "*", "-"], [2, 3, 4, 5], 9),         # 2 + 3 * 4 - 5 = 9
        # Floor division
        (["//"], [9, 2], 4),                        # 9 // 2 = 4
        # Exponentiation
        (["**"], [2, 3], 8),                        # 2 ** 3 = 8
        # Combination with exponent and multiplication
        (["**", "*"], [2, 3, 4], 32),               # 2 ** 3 * 4 = 32
        # Chain of same operator
        (["+", "+", "+"], [1, 2, 3, 4], 10),        # 1 + 2 + 3 + 4 = 10
        # Division after multiplication (checks left‑to‑right evaluation)
        (["*", "//"], [8, 3, 2], 12),               # 8 * 3 // 2 = 12
        # Exponent after addition (addition first, then exponent)
        (["+", "**"], [2, 3, 2], 25),               # 2 + 3 ** 2 = 11? Wait precedence: 3**2=9, 2+9=11
                                                    # Actually Python precedence makes ** first, so result = 2 + (3**2) = 11
                                                    # We'll assert 11.
        # Large numbers
        (["*", "**"], [10, 2, 3], 1000),            # 10 * 2 ** 3 = 80? Actually 2**3=8, 10*8=80. Use 10**2 * 3 = 300? Let's pick a clear case:
                                                    # Use operators ["**", "*"] with operands [10, 2, 3] => 10**2 * 3 = 300
        (["**", "*"], [10, 2, 3], 300),
    ],
)
def test_do_algebra_various(operators, operands, expected):
    # Adjust the expected value for the case where precedence matters.
    # The function builds a Python expression string and evaluates it,
    # so Python's operator precedence applies.
    result = do_algebra(operators, operands)
    assert result == expected


def test_do_algebra_invalid_lengths():
    """The function should raise a ValueError when the lengths don't match the contract."""
    with pytest.raises(ValueError):
        do_algebra(["+", "-"], [1, 2])  # operators length 2, operands length 2 -> mismatch


def test_do_algebra_unsupported_operator():
    """If an unsupported operator is supplied, a ValueError should be raised."""
    with pytest.raises(ValueError):
        do_algebra(["%"], [5, 2])  # modulo is not in the allowed list


def test_do_algebra_non_integer_operands():
    """Operands must be integers; passing a non‑integer should raise a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(["+"], [1, "two"])


def test_do_algebra_empty_operator_list():
    """Operator list must contain at least one operator."""
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])