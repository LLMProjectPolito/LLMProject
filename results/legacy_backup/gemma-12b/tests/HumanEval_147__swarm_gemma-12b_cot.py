import pytest
import math

def test_get_max_triples_n_equals_2():
    """Test case for n = 2, where no triples are possible."""
    assert get_max_triples(2) == 0