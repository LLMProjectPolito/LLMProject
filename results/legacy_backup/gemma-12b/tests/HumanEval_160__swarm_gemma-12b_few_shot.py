import pytest
import math

def test_do_algebra_exponentiation_edge():
    assert do_algebra(['**'], [2, 3]) == 8