import pytest
import math

import pytest

def test_basic():
    assert get_max_triples(5) == 1

import pytest

def test_edge_empty():
    assert get_max_triples(0) == 0

import pytest

def test_get_max_triples_invalid_n():
    with pytest.raises(Exception):
        get_max_triples(0)