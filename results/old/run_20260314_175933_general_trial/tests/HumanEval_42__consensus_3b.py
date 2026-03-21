import pytest

@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),
    ([1], [2]),
    ([1, 2, 3], [2, 3, 4]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124]),
    ([-1, -2, -3], [0, -1, -2]),
    ([0, 0, 0], [1, 1, 1]),
    ([1, 2, 3.0], pytest.raises(TypeError)),
    ([1, 'a', 3], pytest.raises(TypeError)),
    ([1, [2], 3], pytest.raises(TypeError)),
])
def test_incr_list(input_list, expected_output):
    if isinstance(expected_output, type(())):
        with pytest.raises(expected_output):
            incr_list(input_list)
    else:
        assert incr_list(input_list) == expected_output