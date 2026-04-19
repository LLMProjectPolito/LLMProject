
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
import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    # Replace 3 or more spaces with a single hyphen
    res = re.sub(r' {3,}', '-', text)
    # Replace remaining single or double spaces with underscores
    res = res.replace(' ', '_')
    return res

@pytest.mark.parametrize("input_text, expected_output", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge Cases: Empty and No Spaces
    ("", ""),
    ("NoSpacesHere", "NoSpacesHere"),
    ("Pytest", "Pytest"),
    ("12345", "12345"),
    
    # Single and Double Spaces (Should be underscores)
    (" ", "_"),
    ("  ", "__"),
    ("Word Word", "Word_Word"),
    ("Word  Word", "Word__Word"),
    ("A B", "A_B"),
    ("A  B", "A__B"),
    
    # Three or more spaces (Should be a single hyphen)
    ("   ", "-"),
    ("    ", "-"),
    ("Word   Word", "Word-Word"),
    ("Word    Word", "Word-Word"),
    ("Word     Word", "Word-Word"),
    ("A   B", "A-B"),
    ("A     B", "A-B"),
    ("A          B", "A-B"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("Start   Mid  End", "Start-Mid__End"),
    ("   Leading", "-Leading"),
    ("Trailing   ", "Trailing-"),
    ("   Both   ", "-Both-"),
    ("  A   B  C    D ", "__A-B__C-D_"),
    ("   Leading spaces", "-Leading_spaces"),
    ("Trailing spaces   ", "Trailing_spaces-"),
    ("Multiple   blocks   of   spaces", "Multiple-blocks-of-spaces"),
    ("One space, two  spaces, three   spaces", "One_space,_two__spaces,_three-spaces"),
    
    # Non-space whitespace (should remain untouched)
    ("Tab\tSpace", "Tab\tSpace"),
    ("Newline\nSpace", "Newline\nSpace"),
    
    # Special characters, numbers, and complex strings
    ("Hello World!  How are   you?", "Hello_World!__How_are-you?"),
    ("1 2  3   4    5", "1_2__3-4-5"),
    ("The quick brown  fox    jumps over the lazy   dog", 
     "The_quick_brown__fox-jumps_over_the_lazy-dog"),
])
def test_fix_spaces(input_text, expected_output):
    """Tests various space configurations to ensure correct replacement logic."""
    assert fix_spaces(input_text) == expected_output

def test_fix_spaces_idempotency():
    """
    Verify that applying the function twice doesn't change the result 
    since underscores and hyphens are not spaces.
    """
    text = "  Mixed   spacing  test    here "
    first_pass = fix_spaces(text)
    assert fix_spaces(first_pass) == first_pass

def test_fix_spaces_large_input():
    """Test with a very large number of consecutive spaces."""
    large_spaces = " " * 1000
    assert fix_spaces(large_spaces) == "-"

def test_fix_spaces_non_string_input():
    """Verify that the function raises a TypeError when non-string input is provided."""
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)