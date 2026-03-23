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
# but handles consecutive spaces differently.  If there are 2 or fewer consecutive spaces,
# it replaces them with underscores. If there are more than 2 consecutive spaces,
# it replaces them with hyphens.
# We need to test various scenarios:
# 1. No spaces: The input string should remain unchanged.
# 2. Single space: The space should be replaced with an underscore.
# 3. Two spaces: The two spaces should be replaced with two underscores.
# 4. More than two spaces: The consecutive spaces should be replaced with hyphens.
# 5. Leading/trailing spaces: The leading and trailing spaces should be handled correctly.
# 6. Mixed spaces: A combination of single, double, and multiple spaces should be tested.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_two_spaces: Tests the case where the input string has two spaces.
# - test_multiple_spaces: Tests the case where the input string has more than two spaces.
# - test_leading_trailing_spaces: Tests the case where the input string has leading and trailing spaces.
# - test_mixed_spaces: Tests a combination of different space scenarios.

### STEP 3: CODE
###
# test_no_spaces.py
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

# test_single_space.py
def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

# test_two_spaces.py
def test_two_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

# test_multiple_spaces.py
def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# test_leading_trailing_spaces.py
def test_leading_trailing_spaces():
    assert fix_spaces("  Hello World  ") == "_Hello_World_"

# test_mixed_spaces.py
def test_mixed_spaces():
    assert fix_spaces("This  is   a test") == "This__is___a_test"