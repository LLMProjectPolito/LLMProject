
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
    # Then replace remaining single or double spaces with '_'
    # We use a regex that finds 3+ spaces first, then handles the rest.
    
    # This regex finds sequences of 3 or more spaces
    res = re.sub(r' {3,}', '-', text)
    # This replaces remaining spaces with underscores
    res = res.replace(' ', '_')
    return res

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge Case: Empty string
    ("", ""),
    
    # Edge Case: No spaces
    ("HelloWorld", "HelloWorld"),
    
    # Edge Case: Only spaces
    (" ", "_"),            # 1 space -> _
    ("  ", "__"),          # 2 spaces -> __ (not more than 2)
    ("   ", "-"),          # 3 spaces -> -
    ("    ", "-"),         # 4 spaces -> -
    ("     ", "-"),        # 5 spaces -> -
    
    # Edge Case: Leading and Trailing spaces
    ("  start", "__start"),
    ("end  ", "end__"),
    ("   both   ", "-both-"),
    
    # Edge Case: Mixed space counts
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   1  2   3 4    5  6", "-1__2-3_4-5__6"),
    
    # Edge Case: Non-space whitespace (should remain untouched based on prompt)
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected