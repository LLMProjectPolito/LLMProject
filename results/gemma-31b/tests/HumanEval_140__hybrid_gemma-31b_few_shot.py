
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
    # --- No Spaces / Empty ---
    ("", ""),
    ("Example", "Example"),
    ("Python123", "Python123"),
    
    # --- Single Spaces (1 space -> _) ---
    (" ", "_"),
    ("A B", "A_B"),
    (" Example", "_Example"),
    ("Example ", "Example_"),
    ("A B C", "A_B_C"),
    
    # --- Double Spaces (2 spaces -> __) ---
    ("  ", "__"),
    ("A  B", "A__B"),
    ("  Example", "__Example"),
    ("Example  ", "Example__"),
    
    # --- Multiple Spaces (3+ spaces -> -) ---
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    ("A   B", "A-B"),
    ("A    B", "A-B"),
    ("   Example", "-Example"),
    ("Example   ", "Example-"),
    
    # --- Mixed Patterns ---
    ("A B  C   D", "A_B__C-D"),
    ("   A  B C   ", "-A__B_C-"),
    ("Hello   World  Test Space", "Hello-World__Test_Space"),
    ("  hello   world  !", "__hello-world__!"),
    ("   leading and   trailing   ", "-leading_and-trailing-"),
    ("A B  C   D    E", "A_B__C-D-E"),
])
def test_fix_spaces(input_text, expected):
    """
    Comprehensive test suite for fix_spaces.
    Rules:
    - 1 space  -> '_'
    - 2 spaces -> '__'
    - 3+ spaces -> '-'
    """
    assert fix_spaces(input_text) == expected