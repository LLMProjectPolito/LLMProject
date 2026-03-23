import pytest
import math

def test_simplify_large_numbers():
    assert simplify("999999999999999/1", "1/999999999999999") == True