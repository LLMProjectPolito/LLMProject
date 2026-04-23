
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

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge Case: Empty string
    ("", ""),
    
    # Edge Case: Single space
    (" ", "_"),
    
    # Edge Case: Exactly two spaces (should be underscores)
    ("  ", "__"),
    
    # Edge Case: Exactly three spaces (more than 2, should be hyphen)
    ("   ", "-"),
    
    # Edge Case: More than three spaces
    ("    ", "-"),
    ("     ", "-"),
    
    # Mixed scenarios
    ("A B  C   D", "A_B__C-D"),
    ("A B    C  D", "A_B-C__D"),
    
    # Leading and Trailing spaces
    ("  Start", "__Start"),
    ("End  ", "End__"),
    ("   Middle   ", "-Middle-"),
    
    # No spaces, only characters
    ("NoSpaces", "NoSpaces"),
    
    # Complex combination
    ("  One  Two   Three    Four ", "__One__Two-Three-Four_"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function for various space configurations:
    - Single spaces -> underscore
    - Exactly two spaces -> two underscores
    - More than two spaces -> single hyphen
    - Leading/trailing spaces
    - Empty strings
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_error():
    """
    Optional: Test if the function handles non-string input if required, 
    though standard implementation assumes string input.
    """
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)