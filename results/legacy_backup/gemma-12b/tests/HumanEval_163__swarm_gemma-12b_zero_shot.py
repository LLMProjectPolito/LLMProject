import pytest
import math

def test_empty_range():
    assert generate_integers(5, 5) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 1) == []