import pytest
import math

def test_fix_spaces_leading_and_trailing():
    assert fix_spaces("  test  ") == "-test-"

def test_fix_spaces_consecutive_at_start():
    assert fix_spaces("   Example") == "-Example"