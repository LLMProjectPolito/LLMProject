
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
import math

import pytest

def test_basic():
    assert fix_spaces("Example 1") == "Example_1"

import pytest

def test_edge_empty_string():
    assert fix_spaces("") == ""

import pytest

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""