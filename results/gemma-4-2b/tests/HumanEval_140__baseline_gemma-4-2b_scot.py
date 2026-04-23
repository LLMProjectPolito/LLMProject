
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

# STEP 1: REASONING
# The function `fix_spaces` takes a string as input and modifies it.
# The goal is to replace spaces with underscores and then replace multiple consecutive spaces with hyphens.
# We need to test various scenarios:
# 1. Empty string: Should return an empty string.
# 2. String with no spaces: Should return the original string.
# 3. String with single spaces: Should replace them with underscores.
# 4. String with multiple spaces: Should replace them with hyphens.
# 5. String with leading/trailing spaces: Should replace them with underscores.
# 6. String with consecutive multiple spaces: Should replace them with hyphens.
# 7. String with a mix of single and multiple spaces.

# STEP 2: PLAN
# We will create pytest test functions for each scenario.
# Each test function will call `fix_spaces` with a specific input and assert the output.

# STEP 3: CODE
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
    for i, char in enumerate(text):
        if char == ' ':
            if i == 0:
                result += "_"
            elif text[i-1] == ' ':
                result += "-"
            else:
                result += "_"
        else:
            result += char
    return result

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_spaces():
    assert fix_spaces("Example ") == "Example_"

def test_multiple_spaces():
    assert fix_spaces("Example   1") == "Example_1"

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_consecutive_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_mixed_spaces():
    assert fix_spaces("Example  123") == "Example_123"

def test_complex_string():
    assert fix_spaces("This   is a   test   string.") == "This_is_a_test_string."