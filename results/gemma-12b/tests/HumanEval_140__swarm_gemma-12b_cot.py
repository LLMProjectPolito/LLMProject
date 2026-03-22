import pytest
import math

def test_leading_and_trailing_multiple_spaces():
    assert fix_spaces("   Example   ") == "-Example-"

def test_multiple_consecutive_spaces_at_start():
    assert fix_spaces("   Example") == "-Example"