import pytest
from decimal import Decimal

def test_truncate_number_zero():
    """ Test the behavior when input is 0.0 """
    assert truncate_number(0.0) == 0.0

def test_zero_number_edge_case():
    """ Test case for a zero input. The decimal part of zero should be 0."""
    assert truncate_number(0) == 0

def test_truncate_number_edge_case_zero_with_decimal_places():
    """ Test that the function truncates 0.0 correctly """
    assert Decimal('0.0') == truncate_number(0.0), "Expected truncate_number(0.0) to return 0.0"