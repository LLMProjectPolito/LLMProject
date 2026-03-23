import pytest
import math

def test_algebra_exponentiation_zero():
    assert do_algebra(['**'], [2, 0]) == 1