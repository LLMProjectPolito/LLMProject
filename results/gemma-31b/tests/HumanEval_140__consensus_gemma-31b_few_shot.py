
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
    # Base cases from docstring
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and whitespace only
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    
    # Consecutive spaces logic
    ("a b", "a_b"),            # 1 space -> _
    ("a  b", "a__b"),          # 2 spaces -> __
    ("a   b", "a-b"),          # 3 spaces -> -
    ("a    b", "a-b"),         # 4 spaces -> -
    ("a     b", "a-b"),        # 5 spaces -> -
    
    # Positional spaces
    (" Leading space", "_Leading_space"),
    ("Trailing space ", "Trailing_space_"),
    ("  Leading", "__Leading"),
    ("   Leading", "-Leading"),
    ("Trailing  ", "Trailing__"),
    ("Trailing   ", "Trailing-"),
    ("  Both  ", "__Both__"),
    ("   Both   ", "-Both-"),
    ("  Both   ", "__Both-"),
    
    # Mixed patterns and complex strings
    (" a b  c   d    e", "_a_b__c-d-e"),
    ("Hello World  Test   Case", "Hello_World__Test-Case"),
    ("   Start  Middle   End  ", "-Start__Middle-End__"),
    ("A B  C   D", "A_B__C-D"),
    ("Hello    World", "Hello-World"),
    (" a  b   c    d  e ", "_a__b-c-d__e_"),
    ("  a  b   c    d", "__a__b-c-d"),
    ("Hello   World  Test", "Hello-World__Test"),
    ("   Leading and Trailing   ", "-Leading_and_Trailing-"),
    ("Multiple   spaces    here  and there", "Multiple-spaces-here__and_there"),
    
    # Special characters and non-space whitespace
    ("123 456", "123_456"),
    ("!@#   $%^", "!@#-$%^"),
    ("Tab\tSpace", "Tab\tSpace"),
    ("Newline\nSpace", "Newline\nSpace"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected

def test_fix_spaces_none():
    """Ensure the function handles non-string input by raising TypeError."""
    with pytest.raises(TypeError):
        fix_spaces(None)