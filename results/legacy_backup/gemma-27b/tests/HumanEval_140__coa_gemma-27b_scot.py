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
    pass  # Provided function, do not redefine

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_exactly_two_spaces():
    assert fix_spaces("Example  3") == "Example_3"

def test_fix_spaces_many_consecutive_spaces():
    assert fix_spaces("   Example    4   ") == "-Example-4-"

# Focus: Consecutive Spaces
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
    pass  # Provided function definition - do not redefine

def test_consecutive_spaces_more_than_two():
    assert fix_spaces("Example   Test") == "Example-Test"

def test_consecutive_spaces_exactly_two():
    assert fix_spaces("Example  Test") == "Example_Test"

def test_no_consecutive_spaces():
    assert fix_spaces("Example 1 Test") == "Example_1_Test"

# Focus: Leading/Trailing Spaces
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
    pass  # Provided function definition - do not redefine

def test_leading_trailing_spaces_single():
    assert fix_spaces(" Example ") == "_Example_"

def test_leading_trailing_spaces_with_internal():
    assert fix_spaces("  Example 1  ") == "_Example_1_"

def test_leading_trailing_and_multiple_internal():
    assert fix_spaces("  Example   1  ") == "_Example-1_"