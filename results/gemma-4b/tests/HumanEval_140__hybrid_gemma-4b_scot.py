
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
    while True:
        space_indices = [i for i, char in enumerate(text) if char == ' ']
        if not space_indices:
            break
        start = space_indices[0]
        end = space_indices[-1] + 1
        if end - start > 2:
            text = text[:start] + "-" + text[end:]
        else:
            text = text[:start] + "_" + text[end:]
    return text

### SCoT Steps:

### STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string with underscores,
# and if there are more than two consecutive spaces, it replaces them with hyphens.
# The function needs to handle cases with no spaces, single spaces, multiple spaces,
# and more than two consecutive spaces.  The logic should be robust and efficient.
# We need to test various scenarios including empty strings, strings with no spaces,
# strings with single spaces, strings with multiple spaces, and strings with more than two consecutive spaces.

### STEP 2: PLAN
# Test functions:
# - test_empty_string: Tests the case where the input string is empty.
# - test_no_spaces: Tests the case where the input string has no spaces.
# - test_single_space: Tests the case where the input string has a single space.
# - test_multiple_spaces: Tests the case where the input string has multiple spaces.
# - test_more_than_two_spaces: Tests the case where the input string has more than two consecutive spaces.
# - test_mixed_spaces: Tests a combination of spaces and other characters.
# - test_leading_and_trailing_spaces: Tests the case where the string has spaces at the beginning and end.

### STEP 3: CODE
###
# test_empty_string.py
def test_empty_string():
    assert fix_spaces("") == ""

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
    assert fix_spaces("Hello   World!") == "Hello_World!"

# test_leading_and_trailing_spaces.py
def test_leading_and_trailing_spaces():
    assert fix_spaces("  This is a test  ") == "_This_is_a_test_"