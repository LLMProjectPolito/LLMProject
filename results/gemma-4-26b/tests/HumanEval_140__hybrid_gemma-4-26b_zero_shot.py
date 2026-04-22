
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
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    def replacer(match):
        group = match.group(0)
        return '-' if len(group) > 2 else '_' * len(group)

    return re.sub(r' +', replacer, text)

@pytest.mark.parametrize("input_text, expected", [
    # Basic cases
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and minimal strings
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    
    # Space count variations
    ("a b", "a_b"),          # 1 space
    ("a  b", "a__b"),        # 2 spaces
    ("a   b", "a-b"),        # 3 spaces
    ("a    b", "a-b"),       # 4 spaces
    
    # Position variations
    ("  start", "__start"),  # Leading 2 spaces
    ("   start", "-start"),  # Leading 3 spaces
    ("end  ", "end__"),      # Trailing 2 spaces
    ("end   ", "end-"),      # Trailing 3 spaces
    ("  middle  ", "__middle__"),
    
    # Complex and mixed patterns
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   multiple   spaces  ", "-multiple-spaces__"),
    ("One space, two  spaces, three   spaces, four    spaces", 
     "One_space,_two__spaces,_three-spaces,_four-spaces"),
    
    # Numbers and special characters
    ("1 2  3   4    5", "1_2__3-4-5"),
    ("! @ #  $   %", "!_@_#__$-%"),
    ("!@# $ %^&* ( )", "!@#_$_%^&*_(_)")
])
def test_fix_spaces_logic(input_text, expected):
    """Tests the core logic of space replacement rules across various scenarios."""
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_error():
    """Tests that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_immutability():
    """Ensures the original string is not modified (strings are immutable in Python)."""
    original = "Hello   World"
    result = fix_spaces(original)
    assert result == "Hello-World"
    assert original == "Hello   World"

def test_fix_spaces_large_input():
    """Tests with a larger string to ensure regex performance and correctness."""
    # "a " * 100 produces "a_a_a_...a_" (100 times)
    # Followed by 5 spaces and "b"
    input_str = ("a " * 100) + (" " * 5) + "b"
    expected = ("a_" * 100) + "-b"
    assert fix_spaces(input_str) == expected