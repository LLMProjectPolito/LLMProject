import pytest
import math

def test_fix_spaces_leading_and_trailing_multiple_spaces():
    assert fix_spaces("   Example   ") == "-Example-"