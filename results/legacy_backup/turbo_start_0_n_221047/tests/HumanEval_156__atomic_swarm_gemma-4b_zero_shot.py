import pytest
import math

import pytest

def test_basic():
    assert int_to_mini_roman(19) == 'xix'

import pytest

def test_edge_zero():
    assert int_to_mini_roman(0) == ''

import pytest

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
        int_to_mini_roman(-1)
        int_to_mini_roman(1001)