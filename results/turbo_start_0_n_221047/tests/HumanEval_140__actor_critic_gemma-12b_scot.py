import pytest
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    # Single space should be replaced with an underscore.
    assert fix_spaces("Example 1") == "Example_1"

def test_consecutive_spaces():
    # Consecutive spaces should be replaced with a hyphen.
    assert fix_spaces("Example   3") == "Example-3"

def test_leading_spaces():
    # Leading spaces should be replaced with an underscore.
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_spaces():
    # Trailing spaces should be replaced with an underscore.
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_mixed_spaces():
    # Mixed spaces: single -> _, consecutive -> -, leading/trailing -> _
    assert fix_spaces("  Example 1  2   3  ") == "-Example_1_2-3_"

def test_only_spaces():
    # String with only spaces should be replaced with a string of hyphens.
    assert fix_spaces("   ") == "---"

def test_long_string():
    # Test with a long string to check for performance and unexpected behavior.
    long_string = "This is a very long string with many spaces.   It has single spaces, consecutive spaces, and leading/trailing spaces. " * 5
    expected_string = "-This_is_a_very_long_string_with_many_spaces--It_has_single_spaces_consecutive_spaces_and_leading/trailing_spaces- " * 5
    assert fix_spaces(long_string) == expected_string

def test_numbers_only():
    # Numbers and spaces
    assert fix_spaces("1 2 3 4") == "1_2_3_4"

def test_special_characters_only():
    # Special characters and spaces
    assert fix_spaces("!@# $ % ^") == "!@#_$ % ^"

def test_spaces_at_word_boundaries():
    # Spaces directly adjacent to words
    assert fix_spaces(" Example 1 2") == "_Example_1_2"