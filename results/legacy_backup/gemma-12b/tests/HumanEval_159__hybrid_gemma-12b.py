import pytest
from your_module import eat  # Replace your_module

class TestEat:
    """
    Comprehensive pytest suite for the eat function.
    """

    def test_basic_cases(self):
        """Tests basic scenarios with sufficient remaining carrots."""
        assert eat(5, 6, 10) == [11, 4]
        assert eat(4, 8, 9) == [12, 1]
        assert eat(1, 10, 10) == [11, 0]
        assert eat(2, 11, 5) == [7, 0]

    def test_insufficient_remaining_carrots(self):
        """Tests cases where remaining carrots are less than needed."""
        assert eat(5, 12, 3) == [8, 0]
        assert eat(0, 5, 2) == [2, 0]
        assert eat(10, 20, 5) == [15, 0]

    def test_no_remaining_carrots(self):
        """Tests cases where there are no remaining carrots."""
        assert eat(5, 6, 0) == [5, 0]
        assert eat(0, 5, 0) == [0, 0]
        assert eat(10, 10, 0) == [10, 0]

    def test_already_met_need(self):
        """Tests cases where the rabbit has already eaten enough carrots."""
        assert eat(10, 5, 5) == [10, 5]
        assert eat(20, 10, 10) == [20, 10]
        assert eat(5, 5, 0) == [5, 0]

    def test_zero_input_values(self):
        """Tests cases with zero input values."""
        assert eat(0, 0, 0) == [0, 0]
        assert eat(0, 5, 10) == [5, 10]
        assert eat(5, 0, 10) == [5, 10]
        assert eat(5, 5, 0) == [5, 0]

    def test_edge_cases(self):
        """Tests edge cases at the boundaries of the constraints."""
        assert eat(0, 0, 1000) == [0, 1000]
        assert eat(1000, 1000, 1000) == [2000, 0]
        assert eat(1000, 1001, 1000) == [2000, 0]
        assert eat(0, 1000, 0) == [0, 0]
        assert eat(1000, 0, 0) == [1000, 0]

    def test_large_numbers(self):
        """Tests with larger numbers within the constraints."""
        assert eat(500, 600, 1000) == [1100, 400]
        assert eat(900, 1000, 500) == [1400, 0]

    def test_negative_input_raises_error(self):
        """Tests that negative inputs raise a ValueError."""
        with pytest.raises(ValueError):
            eat(-1, 5, 10)
        with pytest.raises(ValueError):
            eat(5, -1, 10)
        with pytest.raises(ValueError):
            eat(5, 5, -1)

    def test_non_integer_input_raises_error(self):
        """Tests that non-integer inputs raise a TypeError."""
        with pytest.raises(TypeError):
            eat(5.5, 6, 10)
        with pytest.raises(TypeError):
            eat(5, 6.5, 10)
        with pytest.raises(TypeError):
            eat(5, 6, 10.5)