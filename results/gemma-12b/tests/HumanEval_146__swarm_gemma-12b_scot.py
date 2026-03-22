import pytest
import math

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0