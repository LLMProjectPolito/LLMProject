import pytest
import math

def test_n_equals_2():
    """Test case for n = 2, which should return 0 because there are not enough elements to form a triple."""
    assert get_max_triples(2) == 0