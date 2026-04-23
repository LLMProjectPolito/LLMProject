
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
    # This is the implementation being tested. 
    # Note: The implementation is not provided in the prompt, 
    # so this suite is designed to validate the logic described.
    import re
    # Replace more than 2 spaces with '-'
    text = re.sub(r' {3,}', '-', text)
    # Replace remaining single/double spaces with '_'
    text = text.replace(' ', '_')
    return text

@pytest.mark.parametrize("input_str, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Boundary: Exactly 1 space
    ("a b", "a_b"),
    
    # Boundary: Exactly 2 spaces (Not "more than 2", so should be underscores)
    ("a  b", "a__b"),
    
    # Boundary: Exactly 3 spaces (More than 2, should be dash)
    ("a   b", "a-b"),
    
    # Boundary: 4 spaces (More than 2, should be dash)
    ("a    b", "a-b"),
    
    # Mixed patterns
    ("a b  c   d    e", "a_b__c-d-e"),
    
    # Leading and Trailing
    ("   start", "-start"),
    ("end   ", "end-"),
    ("  middle  ", "__middle__"),
    ("   both   ", "-both-"),
])
def test_fix_spaces_logic(input_str, expected):
    """Tests the core logic requirements and boundary conditions for space counts."""
    assert fix_spaces(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                          # Empty string
    (" ", "_"),                        # Single space
    ("  ", "__"),                      # Double space
    ("   ", "-"),                      # Triple space
    ("    ", "-"),                     # Quadruple space
    ("a", "a"),                        # No spaces
    ("!@# $%^", "!@#_%^"),             # Special characters
    ("1 2 3", "1_2_3"),                # Numbers
])
def test_fix_spaces_edge_cases(input_str, expected):
    """Tests edge cases like empty strings, single characters, and special symbols."""
    assert fix_spaces(input_str) == expected

def test_fix_spaces_immutability():
    """Ensure the function does not mutate the input if it were a mutable type (though strings are immutable)."""
    original = "Hello   World"
    result = fix_spaces(original)
    assert original == "Hello   World"
    assert result == "Hello-World"

def test_fix_spaces_large_input():
    """Test with a larger string to ensure performance and correctness."""
    large_input = "a " * 100 + " " * 5 + "b"
    # "a " * 100 creates "a a a..." (99 single spaces and 1 trailing space)
    # Then we add 5 spaces and "b"
    # The 5 spaces should become "-"
    # The "a " parts should become "a_"
    expected_part = "a_" * 100
    expected = expected_part + "-b"
    assert fix_spaces(large_input) == expected