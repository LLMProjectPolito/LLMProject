
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

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    import re
    # Replace 3 or more spaces with '-'
    # Then replace remaining single spaces with '_'
    # We use a regex with a lookahead or a specific order to ensure 
    # that sequences of 3+ are handled before single/double spaces.
    
    # First, handle the 3+ spaces case
    text = re.sub(r' {3,}', '-', text)
    # Then, handle the remaining spaces (1 or 2)
    text = text.replace(' ', '_')
    return text

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge Case: Empty string
    ("", ""),
    
    # Edge Case: Only spaces
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    
    # Edge Case: Exactly 2 spaces (should be underscores, as 2 is not > 2)
    ("Hello  World", "Hello__World"),
    
    # Edge Case: Exactly 3 spaces (should be hyphen)
    ("Hello   World", "Hello-World"),
    
    # Edge Case: More than 3 spaces (should be hyphen)
    ("Hello    World", "Hello-World"),
    ("Hello     World", "Hello-World"),
    
    # Edge Case: Leading and Trailing spaces
    ("   Leading", "-Leading"),
    ("Trailing   ", "Trailing-"),
    ("  Both  ", "__Both__"),
    ("   Both   ", "-Both-"),
    
    # Complex mixed cases
    (" a b  c   d    e ", "_a_b__c-d-e_"),
    ("Multiple   spaces and  two spaces", "Multiple-spaces_and__two_spaces"),
    ("   Three   and    Four   ", "-Three-and-Four-"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected