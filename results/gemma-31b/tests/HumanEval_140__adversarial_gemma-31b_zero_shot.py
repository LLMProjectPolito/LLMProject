
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
    # This is the implementation to be tested. 
    # If the function is provided externally, this block would be omitted.
    import re
    # Replace 3 or more spaces with '-'
    text = re.sub(r' {3,}', '-', text)
    # Replace remaining spaces (1 or 2) with '_'
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
    
    # Edge Case: No spaces
    ("HelloWorld", "HelloWorld"),
    
    # Single space cases
    (" ", "_"),
    ("a b", "a_b"),
    
    # Two consecutive spaces (Should be underscores, as it's not MORE than 2)
    ("  ", "__"),
    ("a  b", "a__b"),
    
    # Three consecutive spaces (Should be hyphen)
    ("   ", "-"),
    ("a   b", "a-b"),
    
    # More than three consecutive spaces (Should be single hyphen)
    ("    ", "-"),
    ("a     b", "a-b"),
    
    # Mixed space counts
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   a  b c   ", "-a__b_c-"),
    
    # Leading and trailing spaces
    ("  start", "__start"),
    ("end  ", "end__"),
    ("   start", "-start"),
    ("end   ", "end-"),
    
    # Strings with other whitespace characters (should remain untouched)
    ("a\tb", "a\tb"),
    ("a\nb", "a\nb"),
    
    # Complex combination
    ("  Hello   World  Test    Done ", "__Hello-World__Test-Done_"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected