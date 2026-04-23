
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

# The function is assumed to be imported from the source module
# from solution import fix_spaces

@pytest.mark.parametrize("input_text, expected", [
    # --- Provided Examples ---
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # --- Boundary Case: Exactly 2 spaces ---
    # The rule says "more than 2" for hyphens, so 2 spaces should be underscores
    ("a  b", "a__b"), 
    
    # --- Boundary Case: Exactly 3 spaces (The threshold) ---
    ("a   b", "a-b"),
    
    # --- Boundary Case: More than 3 spaces ---
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    
    # --- Edge Case: Spaces at the start and end ---
    ("   start", "-start"),
    ("end   ", "end-"),
    ("  middle  ", "__middle__"),
    ("   both   ", "-both-"),
    
    # --- Edge Case: Mixed clusters ---
    # 1 space -> _, 2 spaces -> __, 3 spaces -> -, 4 spaces -> -
    ("a b  c   d    e", "a_b__c-d-e"),
    
    # --- Edge Case: Empty and No-Space strings ---
    ("", ""),
    ("NoSpaces", "NoSpaces"),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    
    # --- Edge Case: Non-alphanumeric characters ---
    ("! @ #", "!_@_#"),
    ("!   @   #", "!-@-#"),
    
    # --- Edge Case: Tabs and Newlines (Should NOT be treated as spaces) ---
    # Standard requirement usually implies the literal space character ' '
    ("a\tb", "a\tb"),
    ("a\n b", "a\n_b"),
])
def test_fix_spaces_logic(input_text, expected):
    """
    Tests various combinations of space counts to ensure the 
    'more than 2' rule and the 'single hyphen' rule are implemented correctly.
    """
    from solution import fix_spaces # Adjust import as necessary
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_safety():
    """
    Blue Team check: How does the function handle non-string inputs?
    (Depending on strictness, this might be expected to raise a TypeError)
    """
    from solution import fix_spaces
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_immutability():
    """
    Ensure the function returns a new string and doesn't attempt 
    to mutate anything (though strings are immutable in Python, 
    this is a good practice for complex objects).
    """
    from solution import fix_spaces
    original = "Hello   World"
    result = fix_spaces(original)
    assert result != original
    assert original == "Hello   World"