import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the location of the implementation.
# For example, if the function lives in `my_module.py`, replace the line
# with: `from my_module import fix_spaces`
# ----------------------------------------------------------------------
from fix_spaces import fix_spaces   # <-- change if necessary


@pytest.mark.parametrize(
    "input_text, expected",
    [
        # No spaces – the string should be returned unchanged
        ("Example", "Example"),
        ("", ""),

        # Single spaces become underscores
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        ("Example ", "Example_"),
        ("  Leading", "__Leading"),

        # Exactly two consecutive spaces – each becomes an underscore
        ("Example  2", "Example__2"),
        ("A  B", "A__B"),

        # More than two consecutive spaces – the whole run is replaced by '-'
        ("Example   3", "Example-3"),
        ("A   B", "A-B"),
        ("Hello    World", "Hello-World"),   # 4 spaces → single '-'

        # Mixed runs of spaces
        ("  A   B  C ", "__A-B__C_"),
        ("Start   middle  end", "Start-middle__end"),

        # String consisting only of spaces
        (" ", "_"),
        ("  ", "__"),
        ("   ", "-"),
        ("    ", "-"),   # any run >2 is a single '-'

        # Non‑space whitespace characters should be left untouched
        ("Tab\tSpace", "Tab\tSpace"),
        ("New\nLine", "New\nLine"),

        # Unicode characters mixed with spaces
        ("Пример  тест", "Пример_тест"),
        ("例子   示例", "例子-示例"),
    ],
)
def test_fix_spaces_various_cases(input_text: str, expected: str) -> None:
    """
    Verify that `fix_spaces` correctly transforms spaces according to the
    specification for a wide range of inputs.
    """
    assert fix_spaces(input_text) == expected


def test_original_string_unchanged() -> None:
    """
    Ensure that the function does not mutate the original string object.
    (Strings are immutable, but this test guards against accidental
    in‑place modifications if the implementation were to use a mutable
    container internally and return the same reference.)
    """
    original = "  mutable?  "
    result = fix_spaces(original)

    # The returned value must be a new string (different identity)
    assert result is not original
    # The original value must stay exactly the same
    assert original == "  mutable?  "


def test_long_string_performance() -> None:
    """
    A very long string with many space runs should still be processed
    correctly and efficiently. The test checks correctness rather than
    strict timing, but it also guards against pathological O(n²) behaviour
    that could cause the test to hang.
    """
    # Build a string: 1000 groups of "a   " (3 spaces) followed by "b"
    long_input = ("a   " * 1000) + "b"
    # Expected: each "a   " becomes "a-" and final "b" stays
    expected = ("a-" * 1000) + "b"

    assert fix_spaces(long_input) == expected