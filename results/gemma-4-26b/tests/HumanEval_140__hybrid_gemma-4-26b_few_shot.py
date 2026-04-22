
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

# Assuming fix_spaces is imported from your module
# from your_module import fix_spaces

@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                   # Empty string
    ("Example", "Example"),     # No spaces
    ("abc123XYZ", "abc123XYZ"), # Alphanumeric
    ("12345", "12345"),         # Numbers
    ("a-b", "a-b"),             # Existing hyphens
    ("a_b", "a_b"),             # Existing underscores
    (" _ ", "_-_"),             # Mixed existing underscores/spaces
])
def test_fix_spaces_identity(input_str, expected):
    """Tests strings that should remain unchanged or contain no spaces."""
    assert fix_spaces(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    # Rule: 1 space -> "_"
    (" ", "_"),
    ("a b", "a_b"),
    (" Hello ", "_Hello_"),
    
    # Rule: 2 spaces -> "__"
    ("  ", "__"),
    ("a  b", "a__b"),
    ("  start", "__start"),
    ("end  ", "end__"),
    ("  test  ", "__test__"),
    
    # Rule: 3 or more spaces -> "-"
    ("   ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),  # 4 spaces
    ("a     b", "a-b"), # 5 spaces
    ("      ", "-"),    # 6 spaces
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),
])
def test_fix_spaces_logic(input_str, expected):
    """Tests the core logic: 1 space (_), 2 spaces (__), and 3+ spaces (-)."""
    assert fix_spaces(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    # Mixed 1, 2, and 3+ patterns
    ("a b  c   d", "a_b__c-d"),
    ("a b  c   d e", "a_b__c-d_e"),
    ("  word    next  ", "__word-next__"),
    ("   start  middle end ", "-start__middle_end_"),
])
def test_fix_spaces_complex_patterns(input_str, expected):
    """Tests complex strings containing various sequences of spaces."""
    assert fix_spaces(input_str) == expected