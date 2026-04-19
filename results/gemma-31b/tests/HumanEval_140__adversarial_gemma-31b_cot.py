
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

@pytest.mark.parametrize("input_text, expected_output", [
    # Docstring examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and No Spaces
    ("", ""),
    ("Hello", "Hello"),
    ("Hello World", "Hello_World"),
    
    # Edge cases: Single and Double Spaces
    (" ", "_"),
    ("  ", "__"),
    ("a b", "a_b"),
    ("a  b", "a__b"),
    
    # Edge cases: More than 2 consecutive spaces (3+)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    
    # Mixed space lengths
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  abc   def  ghi    jkl ", "__abc-def__ghi-jkl_"),
    ("   a   b   ", "-a-b-"),
    ("  a  b  ", "__a__b__"),
    (" a b ", "_a_b_"),
    
    # Leading and Trailing spaces
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),
    ("  both  ", "__both__"),
    ("   both   ", "-both-"),
    
    # Complex combinations
    ("One space, two  spaces, three   spaces, four    spaces", 
     "One_space,_two__spaces,_three-spaces,_four-spaces"),
    ("   Multiple   groups   of   spaces   ", "-Multiple-groups-of-spaces-"),
])
def test_fix_spaces(input_text, expected_output):
    """
    Tests the fix_spaces function against various scenarios:
    - No spaces
    - Single spaces (should become _)
    - Double spaces (should become __ as they are not 'more than 2')
    - 3 or more spaces (should become -)
    - Mixed combinations of space lengths
    - Leading and trailing spaces
    """
    assert fix_spaces(input_text) == expected_output

def test_fix_spaces_non_string():
    """
    Test how the function handles non-string inputs.
    Depending on implementation, it should either raise a TypeError 
    or handle it gracefully.
    """
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)