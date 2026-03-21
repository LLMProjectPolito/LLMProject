import pytest
import math

def test_rolling_max_single_element_sequence():
    """ Test rolling max on a sequence with a single element """
    assert rolling_max([5]) == [5]

def test_rolling_max_empty_list():
    """ Test for an empty list as input """
    assert rolling_max([]) == []