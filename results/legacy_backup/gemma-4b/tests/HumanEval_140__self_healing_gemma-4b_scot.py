import pytest

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
    while "  " in text:
        text = text.replace("  ", "-")
    return text.replace(" ", "_")

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` takes a string as input and modifies it by replacing spaces with underscores.
# If there are more than two consecutive spaces, it replaces them with hyphens.
# The tests should cover various scenarios including:
# 1. No spaces in the input string.
# 2. Single space in the input string.
# 3. Multiple spaces in the input string.
# 4. Consecutive spaces (more than two).
# 5. Mixed spaces and other characters.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces
# - test_single_space
# - test_multiple_spaces
# - test_consecutive_spaces
# - test_mixed_spaces
# - test_empty_string

### STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_mixed_spaces():
    assert fix_spaces("This  is   a  test") == "This_is_a_test"

def test_empty_string():
    assert fix_spaces("") == ""