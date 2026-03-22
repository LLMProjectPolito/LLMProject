import pytest
import math

def test_compare_empty_lists():
    """Test case for empty input lists."""
    game = []
    guess = []
    expected_result = []
    assert compare(game, guess) == expected_result