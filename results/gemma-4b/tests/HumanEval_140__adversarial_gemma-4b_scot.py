
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
    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count <= 2:
                result += '_'
            else:
                result += '-'
        else:
            result += char
            count = 0
    return result

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string with underscores,
# but if there are more than two consecutive spaces, it replaces them with hyphens.
# We need to test various scenarios including:
# 1. No spaces in the input string.
# 2. Single space in the input string.
# 3. Multiple spaces in the input string.
# 4. More than two consecutive spaces.
# 5. Leading and trailing spaces.
# 6. Mixed spaces and other characters.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Checks the case with no spaces.
# - test_single_space: Checks the case with a single space.
# - test_multiple_spaces: Checks the case with multiple spaces.
# - test_more_than_two_spaces: Checks the case with more than two consecutive spaces.
# - test_leading_trailing_spaces: Checks the case with leading and trailing spaces.
# - test_mixed_spaces: Checks the case with mixed spaces and other characters.

### STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_more_than_two_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_leading_trailing_spaces():
    assert fix_spaces("  Hello World  ") == "_Hello_World_"

def test_mixed_spaces():
    assert fix_spaces("Hello   World!  ") == "Hello-World-!"