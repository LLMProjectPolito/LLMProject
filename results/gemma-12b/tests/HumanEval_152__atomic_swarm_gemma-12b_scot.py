import pytest
import math

def test_compare_positive():
    """Test with a typical positive case where some guesses are correct and some are incorrect."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected_result = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected_result

def test_edge_empty_input():
    """Test with empty input lists."""
    assert compare([], []) == []

def test_compare_invalid_input_types():
    """Test that the function raises a TypeError if the input types are incorrect."""
    import pytest
    with pytest.raises(TypeError):
        compare("123", [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], "123")
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, "a", 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, "b"])