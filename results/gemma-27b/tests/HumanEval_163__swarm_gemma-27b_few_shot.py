import pytest

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []