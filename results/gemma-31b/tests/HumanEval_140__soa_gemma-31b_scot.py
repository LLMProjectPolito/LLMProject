
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
    
    # Edge cases: Number of spaces
    ("", ""),                          # Empty string
    (" ", "_"),                        # Single space
    ("  ", "__"),                      # Exactly 2 spaces (not more than 2)
    ("   ", "-"),                      # Exactly 3 spaces (more than 2)
    ("    ", "-"),                     # More than 3 spaces
    
    # Position of spaces
    ("Leading space", "_Leading_space"),
    ("Trailing space ", "Trailing_space_"),
    ("  Both  ", "__Both__"),          # 2 spaces at start and end
    ("   Both   ", "-Both-"),          # 3 spaces at start and end
    
    # Mixed sequences
    ("a b  c   d    e", "a_b__c-d-e"), # 1, 2, 3, 4 spaces respectively
    ("   a b  c   ", "-a_b__c-"),      # Mixed leading, middle, trailing
    ("   ", "-"),                      # Only 3 spaces
    ("  ", "__"),                      # Only 2 spaces
    
    # Non-space whitespace (should remain unchanged as per "replace all spaces")
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected