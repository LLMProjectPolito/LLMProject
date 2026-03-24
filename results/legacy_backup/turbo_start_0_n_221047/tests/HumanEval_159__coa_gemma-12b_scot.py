import pytest
import math


# Focus: Boundary Values
def test_eat_boundary_need_equals_remaining():
    """Test when need is equal to remaining carrots."""
    assert eat(5, 6, 6) == [11, 0]

def test_eat_boundary_need_slightly_greater_than_remaining():
    """Test when need is slightly greater than remaining carrots."""
    assert eat(2, 11, 10) == [12, 0]

def test_eat_boundary_zero_remaining():
    """Test when there are no remaining carrots."""
    assert eat(5, 6, 0) == [5, 0]

# Focus: Type Scenarios
def test_eat_sufficient_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_insufficient_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exact_need():
    assert eat(1, 10, 10) == [11, 0]

# Focus: Logic Branches
def test_eat_enough_carrots():
    """Test case: Enough carrots remaining to satisfy the need."""
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    """Test case: Not enough carrots remaining, eat all and still hungry."""
    assert eat(2, 11, 5) == [7, 0]

def test_eat_exactly_enough_carrots():
    """Test case: Exactly enough carrots remaining to satisfy the need."""
    assert eat(1, 10, 10) == [11, 0]