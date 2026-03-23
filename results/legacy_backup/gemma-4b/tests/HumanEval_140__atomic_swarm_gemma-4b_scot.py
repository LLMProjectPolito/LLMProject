import pytest
import math

def test_basic():
    assert fix_spaces("Example") == "Example"

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
            count = 0
            result += char
    return result

### SCoT Steps:
### STEP 1: REASONING - The function `fix_spaces` replaces spaces with underscores, but if there are more than two consecutive spaces, it replaces them with a single hyphen. The edge case to test is a string with a very large number of consecutive spaces.
### STEP 2: PLAN - Test function name: `test_many_spaces`. Scenario: Input string with many consecutive spaces.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_many_spaces():
    assert fix_spaces(" " * 100) == "- "

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
            count = 0
            result += char
    return result

### SCoT Steps:
### STEP 1: REASONING - The function replaces spaces with underscores, but if there are more than two consecutive spaces, it replaces them with a hyphen. We need to test the case where there are more than two consecutive spaces to ensure the hyphen replacement works correctly.
### STEP 2: PLAN - Test function name: test_more_than_two_spaces. Scenario: Input string with more than two consecutive spaces.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_more_than_two_spaces():
    assert fix_spaces("Example   3") == "_Example-3"