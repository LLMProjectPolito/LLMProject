import pytest
import math

def test_generate_integers_empty_range():
    assert generate_integers(10, 14) == []