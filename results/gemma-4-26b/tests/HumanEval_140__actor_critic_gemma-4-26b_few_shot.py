
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

# --- The function is assumed to be imported or defined above ---
# def fix_spaces(text): ...

@pytest.mark.parametrize("input_str, expected", [
    # --- Original Logic Tests ---
    # No spaces
    ("Example", "Example"),
    ("abc123", "abc123"),
    ("", ""),
    
    # Single space -> _
    ("Example 1", "Example_1"),
    ("a b c", "a_b_c"),
    (" ", "_"),
    
    # Double space -> __
    ("a  b", "a__b"),
    ("  word", "__word"),
    ("  ", "__"),
    
    # Triple or more spaces -> -
    ("Example   3", "Example-3"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("     ", "-"),
    ("   ", "-"),
    
    # Leading and Trailing
    (" Example 2", "_Example_2"),
    ("Example ", "Example_"),
    ("   Start", "-Start"),
    ("End   ", "End-"),
    
    # Mixed patterns
    ("a b  c   d", "a_b__c-d"),
    ("  a b   c ", "__a_b-c_"),

    # --- Mixed Whitespace Interaction ---
    # Ensures spaces adjacent to tabs/newlines are treated as individual 
    # spaces unless the spaces themselves are consecutive.
    (" \t ", "_ \t _"),      # Space, Tab, Space (No consecutive spaces)
    ("\t  ", "\t__"),        # Tab, Space, Space (Two consecutive spaces)
    ("  \t", "__\t"),        # Space, Space, Tab (Two consecutive spaces)
    ("   \t", "-\t"),        # Three spaces, then Tab (Three consecutive spaces)
    (" \n ", "_ \n _"),      # Space, Newline, Space
])
def test_fix_spaces_logic(input_str, expected):
    """Tests all valid string scenarios including various space counts and positions."""
    assert fix_spaces(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    # --- Contextual Whitespace Testing ---
    # Verifies that non-space whitespace is preserved when embedded in strings
    ("\t", "\t"),
    ("\n", "\n"),
    ("\r", "\r"),
    ("a\tb", "a\tb"),          # Tab embedded
    ("line1\nline2", "line1\nline2"), # Newline embedded
    ("a \t b", "a_ \t _b"),    # Space, Tab, Space (Spaces are not consecutive)
])
def test_fix_spaces_other_whitespace(input_str, expected):
    """
    Verifies behavior for other whitespace characters. 
    Ensures they are preserved and do not trigger space-replacement logic.
    """
    assert fix_spaces(input_str) == expected

@pytest.mark.parametrize("unicode_str", [
    ("\u00A0"),      # Non-breaking space
    (" \u00A0 "),    # Space, NBSP, Space
    ("\u2003"),      # Em space
])
def test_fix_spaces_unicode(unicode_str):
    """
    Verifies that Unicode whitespace characters are treated as 'other whitespace'
    and not as literal ASCII spaces (' ').
    """
    # Based on the requirement to target literal spaces, 
    # Unicode whitespace should remain unchanged.
    assert fix_spaces(unicode_str) == unicode_str

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    1.23,            # Added float
    True,            # Added bool
    ["a", "b"],
    {"key": "value"},
])
def test_fix_spaces_invalid_types(invalid_input):
    """Verifies that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        fix_spaces(invalid_input)