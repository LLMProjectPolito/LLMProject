
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
    # Basic cases from docstring
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty, no spaces, and whitespace only
    ("", ""),
    ("NoSpaces", "NoSpaces"),
    ("12345", "12345"),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    (" " * 10, "-"),
    
    # Single and double spaces
    ("a b", "a_b"),
    ("a  b", "a__b"),
    
    # Three or more spaces
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    
    # Boundary cases: Start and end of string
    (" Leading", "_Leading"),
    ("Trailing ", "Trailing_"),
    ("  Leading", "__Leading"),
    ("   Leading", "-Leading"),
    ("Trailing  ", "Trailing__"),
    ("Trailing   ", "Trailing-"),
    
    # Mixed scenarios
    ("a b  c   d", "a_b__c-d"),
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  a  b   c  ", "__a__b-c__"),
    ("  a   b  c    d ", "__a-b__c-d_"),
    (" a  b   c    d ", "_a__b-c-d_"),
    ("Multiple   spaces and  some_underscores", "Multiple-spaces_and__some_underscores"),
    ("   Many    spaces    here   ", "-Many-spaces-here-"),
    ("hello   world  test", "hello-world__test"),
    ("  leading and trailing  ", "__leading_and_trailing__"),
    ("more   than   two", "more-than-two"),
    ("just  two", "just__two"),
    ("   start and end   ", "-start_and_end-"),
    
    # Special characters and numbers
    ("Special! @#$ %^&*", "Special!_@#$_%^&*"),
    ("123 456   789", "123_456-789"),
    ("Hello World!", "Hello_World!"),
    ("  123   456  789    000  ", "__123-456__789-000__"),
    
    # Non-space whitespace characters (should remain unchanged)
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
    ("\t\n", "\t\n"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function to ensure:
    1. Single spaces are replaced by underscores.
    2. Exactly two spaces are replaced by two underscores.
    3. Three or more consecutive spaces are replaced by a single hyphen.
    4. Non-space whitespace characters are preserved.
    """
    assert fix_spaces(input_text) == expected