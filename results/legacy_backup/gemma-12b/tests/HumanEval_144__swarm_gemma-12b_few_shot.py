import pytest
import math

def test_simplify_large_numbers():
    assert simplify("1000000/1", "1/1000000") == True