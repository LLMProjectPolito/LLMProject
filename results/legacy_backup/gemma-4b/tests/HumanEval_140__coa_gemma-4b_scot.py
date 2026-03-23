import pytest
import math


# Focus: Boundary Values
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
    while "  " in text:
        text = text.replace("  ", "-")
    return text.replace(" ", "_")

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `fix_spaces` should replace spaces with underscores, and consecutive spaces with hyphens.
### We need to test boundary values: empty string, string with no spaces, string with one space, string with two spaces, string with three or more spaces.

### STEP 2: PLAN - List test functions names and scenarios.
### test_fix_spaces_empty
### test_fix_spaces_no_spaces
### test_fix_spaces_single_space
### test_fix_spaces_double_space
### test_fix_spaces_triple_space

### STEP 3: CODE - Write the high-quality pytest suite.
def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_double_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_triple_space():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Type Scenarios
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
    while "  " in text:
        text = text.replace("  ", "-")
    return text.replace(" ", "_")

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_many_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Logic Branches
import pytest

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"