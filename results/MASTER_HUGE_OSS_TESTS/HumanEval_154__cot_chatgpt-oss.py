import pytest

# The function `cycpattern_check` is assumed to be imported from the module under test.
# No import statement is added here per the problem instructions.


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Provided examples
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),

        # Basic edge cases
        ("", "", True),                # both empty -> empty substring
        ("", "a", False),              # a empty, b non‑empty
        ("a", "", True),               # b empty -> empty substring always present
        ("a", "a", True),              # identical single characters
        ("a", "b", False),             # different single characters

        # b longer than a
        ("short", "longerstring", False),

        # Repeated characters
        ("aaaaa", "aa", True),
        ("aaaaa", "aaa", True),
        ("aaaaa", "aaaaaa", False),

        # Rotations that wrap around
        ("abcde", "cdeab", True),      # rotation "abcde" is a substring
        ("abcde", "deabc", True),      # rotation "abcde" again
        ("abcde", "eabcd", True),

        # Rotations that are not present
        ("abcde", "edcba", False),

        # Overlapping occurrences
        ("ababab", "bab", True),       # "bab" is directly present
        ("ababab", "abb", True),       # rotation "abb" appears as "ab[ab]ab"
        ("ababab", "bba", False),

        # Case sensitivity
        ("AbCdEf", "bcd", False),
        ("AbCdEf", "bCd", True),

        # Unicode characters
        ("cafémañana", "ñama", True),  # rotation "mañan" contains "ñama"
        ("cafémañana", "ñamc", False),

        # Large random strings (deterministic for test reproducibility)
        (
            "x" * 1000 + "pattern" + "y" * 1000,
            "tternpa",
            True,
        ),
        (
            "x" * 5000,
            "xxxxx",
            True,
        ),
        (
            "x" * 5000,
            "xyx",
            False,
        ),
    ],
)
def test_cycpattern_check_various(a, b, expected):
    """Test cycpattern_check against a wide range of inputs, focusing on edge and boundary cases."""
    assert cycpattern_check(a, b) is expected


def test_cycpattern_check_rotations_exhaustive():
    """
    Exhaustively verify that for a short string `b`, every rotation is considered.
    The test constructs a string `a` that contains exactly one specific rotation of `b`
    and ensures the function returns True only for that rotation.
    """
    b = "abcd"
    # All rotations of b
    rotations = [b[i:] + b[:i] for i in range(len(b))]
    # Choose a rotation that will be embedded in `a`
    embedded = rotations[2]  # "cdab"
    a = f"xx{embedded}yy"

    for rot in rotations:
        expected = rot == embedded
        assert cycpattern_check(a, rot) is expected


def test_cycpattern_check_no_false_positives_on_substring_overlap():
    """
    Ensure that the function does not mistakenly match across the boundary of a rotation.
    For example, with b = "abc", the rotation "cab" should not be considered present
    in a = "abca" because the substring "cab" would require characters from positions
    2,3,0 which are not contiguous.
    """
    a = "abca"
    b = "abc"
    # Rotations: "abc", "bca", "cab"
    # Only "abc" and "bca" are actual substrings; "cab" is not contiguous.
    assert cycpattern_check(a, b) is True   # "abc" present
    assert cycpattern_check(a, "bca") is True
    assert cycpattern_check(a, "cab") is False