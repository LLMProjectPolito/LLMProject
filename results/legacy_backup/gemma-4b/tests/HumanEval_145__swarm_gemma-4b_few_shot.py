import pytest
import math

def test_order_by_points_empty():
    assert order_by_points([]) == []