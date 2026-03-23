import pytest
import math

def test_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_edge():
    assert eat(0, 0, 0) == [0, 0]

import pytest

def test_eat_negative_remaining():
    """Test case with negative remaining carrots."""
    with pytest.raises(TypeError):
        eat(5, 6, -10)