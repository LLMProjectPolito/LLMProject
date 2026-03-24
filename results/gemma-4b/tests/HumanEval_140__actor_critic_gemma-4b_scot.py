
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
    text = text.replace("  ", "-")
    text = text.replace(" ", "_")
    return text

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string with underscores.
# If there are more than two consecutive spaces, it replaces them with a hyphen.
# We need to test various scenarios including:
# 1. No spaces: The input string has no spaces.
# 2. Single space: The input string has a single space.
# 3. Multiple spaces: The input string has multiple spaces between words.
# 4. Consecutive spaces: The input string has more than two consecutive spaces.
# 5. Leading/trailing spaces: The input string has spaces at the beginning or end.
# 6. Empty string: The input string is empty.
# 7. String with only spaces: The input string contains only spaces.

### STEP 2: PLAN
# Test functions:
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_multiple_spaces: Tests the case where the input string has multiple spaces between words.
# - test_consecutive_spaces: Tests the case where the input string has more than two consecutive spaces.
# - test_leading_trailing_spaces: Tests the case where the input string has spaces at the beginning or end.
# - test_empty_string: Tests the case where the input string is empty.
# - test_only_spaces: Tests the case where the input string contains only spaces.

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

# test_consecutive_spaces.py
def test_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# test_leading_trailing_spaces.py
def test_leading_trailing_spaces():
    assert fix_spaces("  Hello World  ") == "_Hello_World_"

# test_empty_string.py
def test_empty_string():
    assert fix_spaces("") == ""

# test_only_spaces.py
def test_only_spaces():
    assert fix_spaces("   ") == ""

# test_mixed_spaces.py
def test_mixed_spaces():
    assert fix_spaces("Hello  World!  ") == "Hello_World!"