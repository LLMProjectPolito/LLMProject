
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
                result += "_"
            else:
                result += "-"
        else:
            result += char
            count = 0
    return result

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string.
# It handles two specific cases:
# 1. Single spaces are replaced with underscores.
# 2. More than two consecutive spaces are replaced with hyphens.
# The function should handle empty strings and strings with no spaces correctly.
# It should also handle strings with leading/trailing spaces.
# We need to test these scenarios to ensure the function behaves as expected.

### STEP 2: PLAN
# Test cases:
# 1. Empty string: ""
# 2. String with no spaces: "Example"
# 3. String with a single space: "Example 1"
# 4. String with multiple spaces (less than 3): " Example 2"
# 5. String with multiple spaces (exactly 3): " Example   3"
# 6. String with multiple spaces (more than 3): "  Example   Test  "
# 7. String with leading and trailing spaces: "  Leading and trailing spaces  "
# 8. String with only spaces: "   "

# Test function names:
# test_empty_string
# test_no_spaces
# test_single_space
# test_multiple_spaces_less_than_3
# test_multiple_spaces_exactly_3
# test_multiple_spaces_more_than_3
# test_leading_trailing_spaces
# test_only_spaces

### STEP 3: CODE
def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces_less_than_3():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces_exactly_3():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_multiple_spaces_more_than_3():
    assert fix_spaces("  Example   Test  ") == "_Example--Test_"

def test_leading_trailing_spaces():
    assert fix_spaces("  Leading and trailing spaces  ") == "_Leading_and_trailing_spaces_"

def test_only_spaces():
    assert fix_spaces("   ") == "---"