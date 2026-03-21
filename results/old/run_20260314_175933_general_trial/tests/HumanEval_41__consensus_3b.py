import pytest

@pytest.mark.parametrize("n, expected_collisions", [
    (0, 0),
    (1, 1),
    (2, 4),
    (5, 25),
    (10, 100),
    (-1, None),  # Test for negative input
    (1.5, None)  # Test for non-integer input
])
def test_car_race_collision(n, expected_collisions):
    """Test the car_race_collision function for different inputs."""
    if n < 0:
        with pytest.raises(ValueError):
            car_race_collision(n)
    elif not isinstance(n, int):
        with pytest.raises(TypeError):
            car_race_collision(n)
    else:
        assert car_race_collision(n) == n ** 2