def test_compare_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_compare_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_mixed_guesses():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_single_match():
    assert compare([5], [6]) == [1]

def test_compare_single_match_correct():
    assert compare([5], [5]) == [0]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_different_lengths():
    try:
        compare([1, 2], [1])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_compare_negative_scores():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_zero_scores():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3001]) == [0, 0, 1]