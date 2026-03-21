import pytest

def test_basic_cases():
    """Tests basic scenarios with positive numbers."""
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

@pytest.mark.parametrize(
    "number, need, remaining",
    [
        (2, 5, 0),
        (2, 5, 1),
        (2, 5, 5),
        (2, 5, 10),
        (10, 2, 5),
        (5, 10, 2),
    ],
    ids=[
        "number_2_need_5_remaining_0",
        "number_2_need_5_remaining_1",
        "number_2_need_5_remaining_5",
        "number_2_need_5_remaining_10",
        "number_10_need_2_remaining_5",
        "number_5_need_10_remaining_2",
    ],
)
def test_remaining_variations(number, need, remaining):
    """Tests different combinations of number, need, and remaining carrots."""
    expected_eaten = min(number + need, number + remaining)
    expected_remaining = max(0, remaining - (expected_eaten - number))
    assert eat(number, need, remaining) == [expected_eaten, expected_remaining]

def test_zero_cases():
    """Tests scenarios where one or more inputs are zero."""
    assert eat(0, 6, 10) == [6, 4]
    assert eat(5, 0, 10) == [5, 10]
    assert eat(0, 0, 0) == [0, 0]

def test_max_values():
    """Tests scenarios with maximum input values."""
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_large_numbers():
    """Tests scenarios with large input values."""
    assert eat(999, 999, 999) == [1998, 0]
    assert eat(500, 500, 500) == [1000, 0]

def test_negative_number():
    """Tests scenarios with a negative number input."""
    assert eat(-1, 5, 10) == [4, 11]

def test_negative_need():
    """Tests scenarios with a negative need input."""
    assert eat(5, -6, 10) == [-1, 16]

def test_negative_remaining():
    """Tests scenarios with a negative remaining input."""
    assert eat(5, 6, -10) == [5, 0]

def test_negative_all():
    """Tests scenarios with all inputs negative."""
    assert eat(-1, -1, -1) == [-2, 0]

def test_negative_combinations():
    """Tests various combinations of negative inputs."""
    assert eat(-1, 5, -10) == [4, 0]
    assert eat(5, -1, -10) == [4, 0]
    assert eat(-1, -1, 10) == [-2, 12]
    assert eat(5, -6, -1) == [-1, 0]

def test_boundary_large_sum():
    """Tests a boundary condition where the sum of number and need is close to the maximum integer value."""
    assert eat(999, 999, 1) == [1999, 0]

def test_input_validation():
    """Tests for invalid input types."""
    with pytest.raises(TypeError):
        eat("5", 6, 10)
    with pytest.raises(TypeError):
        eat(5, 6.5, 10)
    with pytest.raises(TypeError):
        eat(5, "6", 10)