import pytest
from your_module import compare

def test_compare_equal_length_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_lists_with_same_elements():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_compare_lists_with_most_elements_same():
    assert compare([1, 2, 3, 2, 1], [1, 2, 3, 2, 1]) == [0, 0, 0, 0, 0]

def test_compare_lists_with_duplicates():
    assert compare([1, 2, 2, 3], [1, 2, 2, 3]) == [0, 0, 0, 0]

def test_compare_lists_with_differing_elements():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_lists_with_zero():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_lists_with_negative():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_lists_with_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3000]) == [0, 0, 0]

def test_compare_lists_with_non_numeric_input():
    with pytest.raises(TypeError):
        compare([1, 2, 3], [4, 'a', 6])
    with pytest.raises(TypeError):
        compare([1, 'a', 3], [4, 2, 6])

def test_compare_lists_with_different_lengths():
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])

def test_compare_empty_lists():
    with pytest.raises(ValueError):
        compare([], [1, 2, 3])
    with pytest.raises(ValueError):
        compare([1, 2, 3], [])

def test_compare_lists_with_floats():
    assert compare([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]) == [0.0, 0.0, 0.0]
    assert compare([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == [3.0, 3.0, 3.0]

def test_compare_lists_with_mixed_types():
    with pytest.raises(TypeError):
        compare([1, 2, 3], [4, 'a', 6])

def test_compare_lists_with_non_list_input():
    with pytest.raises(TypeError):
        compare(1, [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], 1)

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_compare_happy_path(game, guess, expected):
    result = compare(game, guess)
    assert result == expected

def test_compare_incorrect_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [2, 2, 0, 3, 3, 4]
    expected = [1, 0, 3, 1, 2, 3]
    result = compare(game, guess)
    assert result == expected

def test_compare_one_zero():
    game = [0, 2, 3, 4, 5, 1]
    guess = [0, 1, 3, 4, 3, -2]
    expected = [0, 1, 0, 0, 2, 3]
    result = compare(game, guess)
    assert result == expected

def test_compare_negative_scores_guesses():
    game = [-1, -2, -3, -4, -5, -1]
    guess = [-1, -2, -3, -4, -5, -2]
    expected = [0, 0, 0, 0, 0, 1]
    result = compare(game, guess)
    assert result == expected

def test_compare_non_integer_scores_guesses():
    game = [1.0, 2.0, 3.0, 4.0, 5.0, 1.0]
    guess = [1.0, 2.0, 3.0, 4.0, 2.0, -2.0]
    expected = [0.0, 0.0, 0.0, 0.0, 3.0, 3.0]
    result = compare(game, guess)
    assert result == expected

def test_compare_unequal_lengths():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2]
    with pytest.raises(ValueError):
        compare(game, guess)

def test_compare_invalid_input():
    game = 123
    guess = [1, 2, 3, 4, 2, -2]
    with pytest.raises(TypeError):
        compare(game, guess)