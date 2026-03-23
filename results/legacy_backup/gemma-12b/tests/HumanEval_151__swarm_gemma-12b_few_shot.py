import pytest
import math

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, 2.5, "a", 3]) == 10