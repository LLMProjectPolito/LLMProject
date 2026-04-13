
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
# The function `fix_spaces` takes a string as input and modifies it according to the following rules:
# 1. Replace all spaces with underscores.
# 2. If there are more than two consecutive spaces, replace them with hyphens.
# We need to create a pytest suite to test these rules with various input strings, including edge cases like empty strings, strings with no spaces, strings with single spaces, strings with multiple spaces, and strings with more than two consecutive spaces.

### STEP 2: PLAN
# Test cases:
# 1. Empty string: ""
# 2. String with no spaces: "Example"
# 3. String with single space: "Example 1"
# 4. String with multiple spaces: " Example 2"
# 5. String with more than two consecutive spaces: " Example   3"
# 6. String with leading and trailing spaces: "  Example  "
# 7. String with mixed spaces: "Hello World"
# 8. String with only spaces: "   "

# Test functions:
# 1. test_empty_string
# 2. test_no_spaces
# 3. test_single_space
# 4. test_multiple_spaces
# 5. test_more_than_two_spaces
# 6. test_leading_trailing_spaces
# 7. test_mixed_spaces
# 8. test_only_spaces

### STEP 3: CODE
def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_more_than_two_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_leading_trailing_spaces():
    assert fix_spaces("  Example  ") == "_Example_"

def test_mixed_spaces():
    assert fix_spaces("Hello World") == "Hello_World"

def test_only_spaces():
    assert fix_spaces("   ") == "--"