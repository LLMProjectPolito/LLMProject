import pytest
import math

def fix_spaces(text):
    """
    Fixes spaces in a string.
    """
    text = text.replace(" ", "")
    return text

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one-one"
    assert fix_spaces("  one  one  ") == "_one-one-one"

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one-one"
    assert fix_spaces("  one  one  ") == "_one-one-one"

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one-one"
    assert fix_spaces("  one  one  ") == "_one-one-one"

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one-one"
    assert fix_spaces("  one  one  ") == "_one-one-one"