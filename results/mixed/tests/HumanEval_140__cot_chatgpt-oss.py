import pytest

# The function `fix_spaces` is assumed to be imported from the module under test.
# e.g., from mymodule import fix_spaces
# No re-definition of the function is performed here.

@pytest.mark.parametrize(
    "text,expected",
    [
        # No spaces
        ("Example", "Example"),
        ("", ""),
        # Single spaces
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        ("Example ", "Example_"),
        ("  ", "__"),                     # two consecutive spaces -> two underscores
        # Exactly two consecutive spaces inside the string
        ("A  B", "A__B"),
        # More than two consecutive spaces
        ("Example   3", "Example-3"),
        (" Example   3", "_Example-3"),
        ("A   B", "A-B"),
        ("A    B", "A-B"),                # four spaces also collapse to a single hyphen
        ("    ", "-"),                    # only spaces, length >2 -> single hyphen
        ("   ", "-"),                     # three spaces -> hyphen
        ("  ", "__"),                     # two spaces -> two underscores
        (" ", "_"),                       # one space -> underscore
        # Mixed runs
        ("A  B   C", "A__B-C"),
        ("A   B  C", "A-B__C"),
        ("  A   B  ", "__A-B__"),
        # Leading and trailing runs of >2 spaces
        ("  Leading", "-Leading"),
        ("Trailing   ", "Trailing-"),
        ("   Both   ", "-Both-"),
        # Non‑space whitespace should be left untouched (function only handles space character)
        ("Line\tTab", "Line\tTab"),
        ("New\nLine", "New\nLine"),
    ],
)
def test_fix_spaces_various_cases(text, expected):
    """Validate that `fix_spaces` correctly transforms spaces according to the specification."""
    assert fix_spaces(text) == expected


def test_fix_spaces_type_error():
    """The function should raise a TypeError when the input is not a string."""
    with pytest.raises(TypeError):
        fix_spaces(123)          # integer
    with pytest.raises(TypeError):
        fix_spaces(None)         # NoneType
    with pytest.raises(TypeError):
        fix_spaces(["a", "b"])   # list