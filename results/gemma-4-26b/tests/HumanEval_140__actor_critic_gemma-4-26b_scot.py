
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest

# The function fix_spaces is assumed to be defined in the environment.

@pytest.mark.parametrize("input_text, expected_output", [
    ("A B", "A_B"),          # 1 space -> _
    ("A  B", "A__B"),        # 2 spaces -> __
    ("A   B", "A-B"),        # 3 spaces -> -
    ("A    B", "A-B"),       # 4 spaces -> -
    ("A      B", "A-B"),     # 6 spaces -> -
])
def test_consecutive_space_logic(input_text, expected_output):
    """Tests the threshold logic for 1, 2, and 3+ consecutive spaces."""
    assert fix_spaces(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("", ""),                # Empty string
    ("NoSpaces", "NoSpaces"), # No spaces
    (" ", "_"),              # Single space only
    ("  ", "__"),            # Two spaces only
    ("   ", "-"),            # Three spaces only
    ("    ", "-"),           # Four spaces only
])
def test_boundary_conditions(input_text, expected_output):
    """Tests edge cases like empty strings and strings containing only spaces."""
    assert fix_spaces(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("  Start", "__Start"),           # Leading 2 spaces
    ("   Start", "-Start"),           # Leading 3 spaces
    ("End  ", "End__"),               # Trailing 2 spaces
    ("End   ", "End-"),               # Trailing 3 spaces
    ("  Mid   End  ", "__Mid-End__"), # Mixed leading, middle, and trailing
])
def test_positional_spaces(input_text, expected_output):
    """Tests spaces located at the start, middle, and end of the string."""
    assert fix_spaces(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("  \t  ", "__\t__"),         # Two spaces, tab, two spaces (interruption)
    ("   \n   ", "-\n-"),         # Three spaces, newline, three spaces (interruption)
    (" \t ", "_\t_"),             # Single space, tab, single space
    ("    \t   ", "-\t-"),        # 4 spaces (becomes -), tab, 3 spaces (becomes -)
])
def test_whitespace_interruption(input_text, expected_output):
    """
    Ensures that non-space whitespace characters interrupt consecutive space sequences,
    preventing them from being counted as a single large block of spaces.
    """
    assert fix_spaces(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ("A\tB", "A\tB"),             # Tab should remain tab
    ("A\nB", "A\nB"),             # Newline should remain newline
    ("A\u00A0B", "A\u00A0B"),     # Non-breaking space should remain non-breaking space
])
def test_whitespace_ambiguity(input_text, expected_output):
    """
    Clarifies that only the literal space character ' ' is replaced.
    Other whitespace characters like \t, \n, and \u00A0 should be ignored.
    """
    assert fix_spaces(input_text) == expected_output

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["a", "b"],
    {"key": "val"},
])
def test_input_type_robustness(invalid_input):
    """Ensures the function raises a TypeError when non-string inputs are provided."""
    with pytest.raises(TypeError):
        fix_spaces(invalid_input)

@pytest.mark.parametrize("input_text, expected_output", [
    ("🚀  🚀", "🚀__🚀"),         # Emojis (Multi-byte)
    ("你好  世界", "你好__世界"),   # CJK Characters
    ("Привет   Мир", "Привет-Мир"), # Cyrillic
    ("!@#  $%^", "!@#__$%^"),     # Special symbols
])
def test_character_set_coverage(input_text, expected_output):
    """Tests that the function handles Unicode and multi-byte characters correctly."""
    assert fix_spaces(input_text) == expected_output

def test_performance_large_input():
    """
    Tests the function with a large input string to ensure efficiency and correctness.
    Verifies that the transformation logic is applied correctly at scale.
    """
    # Create a string of 100,000 characters: "a" followed by 3 spaces, repeated.
    # "a   " (4 chars) becomes "a-" (2 chars).
    iterations = 25000
    large_input = "a   " * iterations 
    expected_output = "a-" * iterations
    
    result = fix_spaces(large_input)
    
    # Verify both length and content to ensure logic wasn't bypassed
    assert len(result) == 50000
    assert result == expected_output