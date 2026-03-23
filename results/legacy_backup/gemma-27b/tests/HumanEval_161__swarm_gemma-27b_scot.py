import pytest

def test_empty_string():
    """
    Test case for an empty string.
    The function should reverse the empty string, which remains empty.
    """
    assert solve("") == ""