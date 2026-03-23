import pytest
import math

def test_eat_need_exceeds_remaining():
    assert eat(2, 11, 5) == [7, 0]