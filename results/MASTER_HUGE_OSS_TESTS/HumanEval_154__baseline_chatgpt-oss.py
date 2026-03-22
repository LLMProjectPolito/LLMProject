import pytest

# Import the function under test.
# Adjust the import path if the implementation lives in a different module.
from solution import cycpattern_check


def brute_cycpattern_check(a: str, b: str) -> bool:
    """
    Reference implementation used only inside the test suite.
    Returns True if any rotation of `b` appears as a substring of `a`.
    """
    if not b:                     # empty pattern is always a substring
        return True
    if len(b) > len(a):
        return False
    # generate all rotations of b
    rotations = {b[i:] + b[:i] for i in range(len(b))}
    return any(rot in a for rot in rotations)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        # edge cases
        ("", "", True),               # both empty
        ("", "a", False),             # a empty, b non‑empty
        ("a", "", True),              # b empty
        ("a", "a", True),             # identical single chars
        ("abc", "cba", True),         # rotation of whole string
        ("aaaaa", "aa", True),        # repeated characters
        ("abcd", "dabc", True),       # rotation that wraps around
        ("abcd", "abcd", True),       # exact match
        ("abcd", "bcda", True),       # rotation that is a substring
        ("abcd", "ac", False),        # non‑contiguous, should be False
        ("xyz", "xyzxyz", False),     # b longer than a
    ],
)
def test_examples_and_edge_cases(a, b, expected):
    """Validate the documented examples and a collection of edge cases."""
    assert cycpattern_check(a, b) is expected


def test_random_strings_against_brute():
    """Compare the implementation with a brute‑force reference on many random inputs."""
    import random
    import string

    for _ in range(200):
        # generate random lengths
        len_a = random.randint(0, 20)
        len_b = random.randint(0, 20)

        a = "".join(random.choice(string.ascii_lowercase) for _ in range(len_a))
        b = "".join(random.choice(string.ascii_lowercase) for _ in range(len_b))

        expected = brute_cycpattern_check(a, b)
        result = cycpattern_check(a, b)

        # The function must return a bool and match the reference result
        assert isinstance(result, bool)
        assert result == expected, f"Failed for a={a!r}, b={b!r}"


def test_rotations_are_handled_correctly():
    """Explicitly verify that each rotation of `b` is considered."""
    a = "thequickbrownfoxjumpsoverthelazydog"
    b = "brown"
    # All rotations of "brown"
    rotations = [b[i:] + b[:i] for i in range(len(b))]
    # Only the original rotation appears in `a`
    assert cycpattern_check(a, b) is True
    # Remove the original rotation from `a` and ensure the function returns False
    a_without = a.replace(b, "")
    assert cycpattern_check(a_without, b) is False
    # Verify that a rotation that does NOT appear also yields False
    for rot in rotations[1:]:
        assert (rot in a) is (rot == b)  # only the original should be present
        assert cycpattern_check(a, rot) is (rot in a)


def test_type_errors_are_not_raised():
    """The function should gracefully handle non‑string inputs by raising TypeError."""
    with pytest.raises(TypeError):
        cycpattern_check(123, "abc")   # a is not a string
    with pytest.raises(TypeError):
        cycpattern_check("abc", None)  # b is not a string