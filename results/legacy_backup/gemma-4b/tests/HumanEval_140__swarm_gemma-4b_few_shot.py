import pytest
import math

def fix_spaces(text):
    return text.replace("  ", " ")

def test_fix_spaces_single_space():
    assert fix_spaces("Example") == "Example"