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
        if char == " ":
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
# The function `fix_spaces` takes a string as input and modifies it by replacing spaces with underscores or hyphens based on the number of consecutive spaces.
# We need to test various scenarios including:
# 1. No spaces in the input string.
# 2. Single space in the input string.
# 3. Multiple spaces in the input string, including cases with more than two consecutive spaces.
# 4. Leading and trailing spaces.
# 5. Mixed spaces and other characters.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_multiple_spaces: Tests the case where the input string has multiple spaces.
# - test_leading_trailing_spaces: Tests the case where the input string has leading and trailing spaces.
# - test_mixed_spaces: Tests the case where the input string has a mix of spaces and other characters.
# - test_consecutive_spaces: Tests the case where the input string has more than two consecutive spaces.

### STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_leading_trailing_spaces():
    assert fix_spaces("  Example  ") == "_Example_"

def test_mixed_spaces():
    assert fix_spaces("Hello World") == "Hello_World"

def test_consecutive_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_empty_string():
    assert fix_spaces("") == ""

def test_multiple_consecutive_spaces():
    assert fix_spaces("This   has    many   spaces") == "This---has----many---spaces"

def test_spaces_at_end():
    assert fix_spaces("Some text   ") == "Some_text-"

def test_spaces_at_beginning():
    assert fix_spaces("   Some text") == "_Some_text-"