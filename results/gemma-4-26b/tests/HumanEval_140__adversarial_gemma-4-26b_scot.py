
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

# The function is provided by the environment; we are writing the test suite.

@pytest.mark.parametrize("input_text, expected_output", [
    # Basic functionality
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    ("Example  2", "Example__2"),
    ("Example   3", "Example-3"),
    ("Example    4", "Example-4"),
    
    # Boundary conditions (The "More than 2" rule)
    ("  ", "__"),          # Exactly 2 spaces -> __
    ("   ", "-"),          # Exactly 3 spaces -> -
    ("    ", "-"),         # Exactly 4 spaces -> -
    
    # Leading and Trailing spaces
    (" Example", "_Example"),
    ("Example ", "Example_"),
    ("  Example", "__Example"),
    ("   Example", "-Example"),
    (" Example   ", "_Example-"),
    
    # Complex mixed patterns
    ("A B  C   D    E", "A_B__C-D-E"),
    ("   A B  C ", "-A_B__C_"),
    
    # Edge cases
    ("", ""),              # Empty string
    (" ", "_"),            # Single space only
    ("  ", "__"),          # Double space only
    ("   ", "-"),          # Triple space only
])
def test_fix_spaces_logic(input_text, expected_output):
    """
    Tests the core logic of space replacement:
    1 space -> _
    2 spaces -> __
    3+ spaces -> -
    """
    from __main__ import fix_spaces # Assuming the function is in the main module
    assert fix_spaces(input_text) == expected_output

def test_fix_spaces_type_safety():
    """
    Blue Team check: Ensure the function handles non-string inputs 
    gracefully if the implementation is expected to be robust, 
    or fails predictably. 
    Note: Based on the prompt, we assume input is always a string.
    """
    from __main__ import fix_spaces
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_immutability():
    """
    Ensure the original string is not mutated (though strings are immutable in Python,
    this is a standard QA check for logic integrity).
    """
    from __main__ import fix_spaces
    original = "Test   String"
    _ = fix_spaces(original)
    assert original == "Test   String"