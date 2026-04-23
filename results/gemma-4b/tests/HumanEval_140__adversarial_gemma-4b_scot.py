
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
            count = 0
            result += char
    return result

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string with underscores,
# but it handles consecutive spaces differently. If there are 2 or fewer consecutive spaces,
# it replaces them with underscores. If there are more than 2 consecutive spaces, it replaces
# them with hyphens.
# We need to test various scenarios:
# 1. Empty string: Should return an empty string.
# 2. String with no spaces: Should return the original string.
# 3. String with single space: Should replace it with an underscore.
# 4. String with two spaces: Should replace them with underscores.
# 5. String with three or more spaces: Should replace them with hyphens.
# 6. String with leading and trailing spaces: Should handle them correctly.
# 7. String with mixed spaces and other characters: Should handle them correctly.

### STEP 2: PLAN
# Test functions:
# - test_empty_string: Tests an empty string input.
# - test_no_spaces: Tests a string with no spaces.
# - test_single_space: Tests a string with a single space.
# - test_two_spaces: Tests a string with two spaces.
# - test_three_spaces: Tests a string with three spaces.
# - test_multiple_spaces: Tests a string with multiple spaces.
# - test_leading_trailing_spaces: Tests a string with leading and trailing spaces.
# - test_mixed_characters: Tests a string with mixed characters and spaces.

### STEP 3: CODE
def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_two_spaces():
    assert fix_spaces("Example 2") == "_Example_2"

def test_three_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_multiple_spaces():
    assert fix_spaces("This  has    many   spaces") == "_This__has___many___spaces"

def test_leading_trailing_spaces():
    assert fix_spaces("  Leading and trailing spaces  ") == "_Leading_and_trailing_spaces_"

def test_mixed_characters():
    assert fix_spaces("Hello World!  123") == "Hello_World!_123"