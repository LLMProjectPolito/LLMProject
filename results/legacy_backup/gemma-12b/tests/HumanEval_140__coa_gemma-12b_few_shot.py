import pytest
import math


# Focus: Boundary Values
def test_fix_spaces_two_consecutive():
    assert fix_spaces("hello  world") == "hello__world"

def test_fix_spaces_three_consecutive():
    assert fix_spaces("hello   world") == "hello-world"

def test_fix_spaces_four_consecutive():
    assert fix_spaces("hello    world") == "hello-world"

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Type Scenarios
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"