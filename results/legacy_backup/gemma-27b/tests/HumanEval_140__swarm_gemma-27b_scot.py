import pytest

def test_leading_and_multiple_spaces(fix_spaces):
    assert fix_spaces("   abc") == "-abc"
    assert fix_spaces("     ") == "-"
    assert fix_spaces("  ") == "_"*2
    assert fix_spaces("   ") == "-"
    assert fix_spaces("  abc") == "_abc"
    assert fix_spaces("   def  ghi") == "-def-ghi"