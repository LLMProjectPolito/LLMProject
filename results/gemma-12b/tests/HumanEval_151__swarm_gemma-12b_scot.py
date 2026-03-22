import pytest
import math

def test_non_integer_list():
    assert double_the_difference([1.5, 2.7, 3.1]) == 0