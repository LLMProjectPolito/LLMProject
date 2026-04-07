
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
# The function `fix_spaces` aims to replace spaces in a string with underscores,
# and if there are more than two consecutive spaces, it replaces them with hyphens.
# We need to test various scenarios including:
# 1. No spaces in the input string.
# 2. Single space in the input string.
# 3. Multiple spaces in the input string.
# 4. More than two consecutive spaces.
# 5. Mixed spaces and other characters.
# 6. Empty string as input.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_multiple_spaces: Tests the case where the input string has multiple spaces.
# - test_more_than_two_spaces: Tests the case where the input string has more than two consecutive spaces.
# - test_mixed_spaces: Tests the case where the input string has a mix of spaces and other characters.
# - test_empty_string: Tests the case where the input string is empty.

### STEP 3: CODE
###
# test_no_spaces.py
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

# test_single_space.py
def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

# test_multiple_spaces.py
def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

# test_more_than_two_spaces.py
def test_more_than_two_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# test_mixed_spaces.py
def test_mixed_spaces():
    assert fix_spaces("Hello   World  !") == "_Hello-World-!"

# test_empty_string.py
def test_empty_string():
    assert fix_spaces("") == ""