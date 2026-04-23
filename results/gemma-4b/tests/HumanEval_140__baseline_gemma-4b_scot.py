
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

### STEP 1: REASONING
# The function `fix_spaces` takes a string as input and modifies it by replacing spaces with underscores or hyphens based on the number of consecutive spaces.
# We need to test various scenarios including:
# 1. No spaces in the input string.
# 2. Single space in the input string.
# 3. Multiple spaces in the input string, including consecutive spaces.
# 4. A mix of spaces and other characters.
# 5. Empty string as input.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_multiple_spaces: Tests the case where the input string has multiple spaces, including consecutive spaces.
# - test_mixed_spaces: Tests the case where the input string has a mix of spaces and other characters.
# - test_empty_string: Tests the case where the input string is empty.

### STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_mixed_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_empty_string():
    assert fix_spaces("") == ""