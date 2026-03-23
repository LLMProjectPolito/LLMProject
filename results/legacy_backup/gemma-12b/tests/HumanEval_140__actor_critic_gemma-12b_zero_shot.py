import pytest
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    """Tests that an empty string returns an empty string."""
    assert fix_spaces("") == ""

def test_no_spaces():
    """Tests that a string with no spaces returns the original string."""
    assert fix_spaces("Example") == "Example"

def test_single_space():
    """Tests that a single space is replaced with an underscore."""
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    """Tests that leading spaces are replaced with hyphens."""
    assert fix_spaces(" Example 2") == "-Example_2"

def test_multiple_spaces():
    """Tests that multiple spaces are replaced with hyphens."""
    assert fix_spaces(" Example   3") == "-Example-3"

def test_multiple_consecutive_spaces():
    """Tests that multiple consecutive spaces are replaced with hyphens."""
    assert fix_spaces("This  is   a    test") == "This-is-a-test"

def test_mixed_spaces():
    """Tests a string with mixed spaces, leading, and trailing spaces."""
    assert fix_spaces("  Hello  World  ") == "-Hello-World-"

def test_only_spaces():
    """Tests a string containing only spaces."""
    assert fix_spaces("   ") == "-"

def test_spaces_at_beginning_and_end():
    """Tests spaces at the beginning and end of the string."""
    assert fix_spaces("  Test  ") == "-Test-"

def test_long_string_with_multiple_spaces():
    """Tests a long string with multiple spaces and consecutive spaces."""
    long_string = "This is a very long string with many spaces.   It has  multiple   consecutive   spaces."
    expected_result = "This-is-a-very-long-string-with-many-spaces.-It-has--multiple---consecutive---spaces."
    assert fix_spaces(long_string) == expected_result

def test_string_with_tabs():
    """Tests that tabs are treated as single spaces and replaced with underscores."""
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    """Tests that newlines are treated as single spaces and replaced with underscores."""
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    """Tests a string with tabs, newlines, and spaces."""
    assert fix_spaces("Example\t 1 \n 2") == "Example_1_2"

def test_string_with_consecutive_spaces_at_start():
    """Tests consecutive spaces at the beginning of the string."""
    assert fix_spaces("   Example") == "-Example"

def test_string_with_consecutive_spaces_at_end():
    """Tests consecutive spaces at the end of the string."""
    assert fix_spaces("Example   ") == "Example-"

def test_string_with_only_tabs_or_newlines():
    """Tests a string containing only tabs or newlines."""
    assert fix_spaces("\t\t") == "--"
    assert fix_spaces("\n\n") == "--"