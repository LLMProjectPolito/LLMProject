import pytest
import math

def test_basic():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_empty_input():
    """Test with empty input lists."""
    game = []
    guess = []
    expected_output = []
    assert compare(game, guess) == expected_output

import pytest

def test_compare_invalid_input_types():
    """Test with invalid input types (e.g., strings instead of lists)."""
    with pytest.raises(TypeError):
        compare("123", [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], "123")
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, "a", 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, 3.5])