import pytest

def test_compare_negative_guess():
    assert compare([1, 2, 3], [1, 2, -3]) == [0, 0, 6]