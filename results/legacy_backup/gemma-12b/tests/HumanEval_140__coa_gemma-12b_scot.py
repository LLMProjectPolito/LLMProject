import pytest
import math


# Focus: Boundary Values
def test_fix_spaces_boundary_zero_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_boundary_two_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_boundary_three_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Type Scenarios
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"