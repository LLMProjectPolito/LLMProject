
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

# The function fix_spaces is already defined in the environment.
# We are writing the test suite to detect bugs in its implementation.

@pytest.mark.parametrize("input_text, expected", [
    # Provided Examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge Case: No spaces
    ("HelloWorld", "HelloWorld"),
    ("", ""),
    
    # Edge Case: Exactly 2 spaces (Should be __ because it's not > 2)
    ("Two  Spaces", "Two__Spaces"),
    ("  ", "__"),
    
    # Edge Case: More than 2 spaces (3, 4, 5...)
    ("Three   Spaces", "Three-Spaces"),
    ("Four    Spaces", "Four-Spaces"),
    ("Many       Spaces", "Many-Spaces"),
    ("   ", "-"),
    
    # Edge Case: Leading and Trailing
    (" Leading", "_Leading"),
    ("Trailing ", "Trailing_"),
    ("  Leading", "__Leading"),
    ("   Leading", "-Leading"),
    ("Trailing  ", "Trailing__"),
    ("Trailing   ", "Trailing-"),
    
    # Complex Mixtures
    (" a  b   c    d", "_a__b-c-d"),
    ("   start  middle   end  ", "-start__middle-end__"),
    ("1 2  3   4    5", "1_2__3-4-5"),
])
def test_fix_spaces_logic(input_text, expected):
    """
    Tests the fix_spaces function against various scenarios including
    single spaces, double spaces, and 3+ consecutive spaces.
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_stability():
    """
    Ensure the function returns a string and handles non-standard 
    but valid string characters.
    """
    result = fix_spaces("Special! @#$   Spaces")
    assert isinstance(result, str)
    assert result == "Special!_@#$-Spaces"

def test_fix_spaces_large_input():
    """
    Test the function with a larger string to ensure no performance 
    bottlenecks or recursion depth issues.
    """
    large_input = "word " * 1000 + "   " + "word"
    # 1000 single spaces -> 1000 underscores, then one sequence of 3 spaces -> hyphen
    expected = "word_" * 1000 + "-word"
    assert fix_spaces(large_input) == expected