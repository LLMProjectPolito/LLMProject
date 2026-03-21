import pytest
import math

import pytest
from typing import List

def test_has_close_elements():
    numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
    threshold = 0.3
    assert has_close_elements(numbers, threshold) == True

import pytest
from typing import List

def test_zero_threshold():
    numbers = [0.0, 0.1, 0.2]
    threshold = 0.0
    expected = True
    assert has_close_elements(numbers, threshold) == expected

import pytest
from typing import List

def test_has_close_elements_empty_list():
    """ Test has_close_elements with an empty list of numbers """
    numbers = []
    threshold = 1.0
    assert not has_close_elements(numbers, threshold)