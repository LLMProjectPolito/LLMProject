import pytest

def test_cycpattern_check_long_a_short_b_no_match():
    assert cycpattern_check("aaaaaaaaab", "bbbb") == False