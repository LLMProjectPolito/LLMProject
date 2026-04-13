
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

# Assuming fix_spaces is imported from your module
# from your_module import fix_spaces

@pytest.mark.parametrize("input_text, expected, scenario", [
    # --- No Spaces ---
    ("Example", "Example", "no spaces"),
    ("", "", "empty string"),
    ("12345", "12345", "numeric string"),

    # --- Single Space (1 -> _) ---
    ("Example 1", "Example_1", "single space middle"),
    (" Example 2", "_Example_2", "single space leading"),
    ("Example 2 ", "Example_2_", "single space trailing"),
    (" ", "_", "single space only"),

    # --- Double Space (2 -> __) ---
    ("Example  2", "Example__2", "double space middle"),
    ("  Example", "__Example", "double space leading"),
    ("Example  ", "Example__", "double space trailing"),
    ("  ", "__", "double space only"),

    # --- Three or More Spaces (3+ -> -) ---
    ("Example   3", "Example-3", "three spaces"),
    ("Example    4", "Example-4", "four spaces"),
    ("Example       5", "Example-5", "many spaces"),
    ("   ", "-", "three spaces only"),
    ("    ", "-", "four spaces only"),
    ("   Leading", "-Leading", "leading 3+ spaces"),
    ("Trailing   ", "Trailing-", "trailing 3+ spaces"),

    # --- Mixed Patterns ---
    ("A B  C   D    E", "A_B__C-D-E", "mixed 1, 2, 3, 4 spaces"),
    ("  Hello   World  ", "__Hello-World__", "mixed leading/trailing"),
    ("  A   B  ", "__A-B__", "mixed double and triple"),
    ("Hello   World   Pytest", "Hello-World-Pytest", "multiple triple blocks"),
    ("Mixed 1  2   3    4", "Mixed_1__2-3-4", "mixed numeric sequence"),
    ("  Start and end  ", "__Start_and_end__", "mixed internal single"),
    ("   Start and end   ", "-Start_and_end-", "mixed internal single with 3+ edges"),
])
def test_fix_spaces_comprehensive(input_text, expected, scenario):
    """
    Comprehensive test suite for fix_spaces.
    Rules:
    - 1 space  -> '_'
    - 2 spaces -> '__'
    - 3+ spaces -> '-'
    """
    assert fix_spaces(input_text) == expected, f"Failed on scenario: {scenario}"