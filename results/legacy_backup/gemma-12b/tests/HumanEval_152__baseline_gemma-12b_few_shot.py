def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_empty():
    assert compare([], []) == []

def test_compare_single_match():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_compare_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed():
    assert compare([1, 2, 3, 4], [1, 5, 3, 2]) == [0, 2, 0, 2]

def test_compare_negative_scores():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_zero_scores():
    assert compare([0, 0, 0], [0, 1, 0]) == [0, 1, 0]

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3001]) == [0, 0, 1]

def test_compare_different_lengths():
    # Should raise an error if lengths are different, but pytest doesn't easily check for that.
    # This test is included to document the expected behavior.
    try:
        compare([1, 2], [1])
        assert False, "Expected ValueError not raised"
    except ValueError:
        pass  # Expected