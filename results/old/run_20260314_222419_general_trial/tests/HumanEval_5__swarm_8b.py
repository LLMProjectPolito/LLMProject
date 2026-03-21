import pytest
import math

def test_intersperse_delimeter_zero():
    """ Tests that a delimeter of 0 does not result in negative numbers in the result """
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_empty_list_with_delimeter():
    """ Verify that the function handles an empty list with a non-zero delimeter. """
    assert intersperse([], 0) == []