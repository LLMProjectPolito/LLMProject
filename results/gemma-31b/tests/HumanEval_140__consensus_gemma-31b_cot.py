
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
    
    # Edge cases: Empty, no spaces, and special characters
    ("", ""),
    ("HelloWorld", "HelloWorld"),
    ("Hello,World!", "Hello,World!"),
    ("12345", "12345"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
    
    # Single spaces (1 -> _)
    (" ", "_"),
    ("Hello World", "Hello_World"),
    (" Hello", "_Hello"),
    ("Hello ", "Hello_"),
    
    # Exactly two consecutive spaces (2 -> __)
    ("  ", "__"),
    ("Hello  World", "Hello__World"),
    ("  Hello", "__Hello"),
    ("Hello  ", "Hello__"),
    
    # Three or more consecutive spaces (3+ -> -)
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    ("Hello   World", "Hello-World"),
    ("Hello    World", "Hello-World"),
    ("   Hello", "-Hello"),
    ("Hello   ", "Hello-"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("  hello   world  ", "__hello-world__"),
    ("one  two   three    four", "one__two-three-four"),
    ("   start and end   ", "-start_and_end-"),
    ("multiple   spaces    here  and there", "multiple-spaces-here__and_there"),
    ("  multiple   spaces  test    ", "__multiple-spaces__test-"),
    ("One space, two  spaces, three   spaces", "One_space,_two__spaces,_three-spaces"),
    ("  One Two   Three    Four", "__One_Two-Three-Four"),
    ("Hello World  This is   a test    string", "Hello_World__This_is-a-test-string"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected