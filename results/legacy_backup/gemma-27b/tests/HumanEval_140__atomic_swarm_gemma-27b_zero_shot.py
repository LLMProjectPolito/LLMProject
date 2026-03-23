import pytest
import math

def test_basic():
    assert fix_spaces("Example 1") == "Example_1"

def test_edge():
    assert fix_spaces("   ") == "-"

def test_more_than_two_consecutive_spaces():
    assert fix_spaces("  abc   def  ") == "-abc-def-"