import pytest

@pytest.mark.parametrize("n, expected_collisions", [
    (1, 1),
    (2, 4),
    (3, 9),
    (5, 25),
    (10, 100)
])
def test_car_race_collision(n, expected_collisions):
    """Test that the function returns the correct number of collisions."""
    assert car_race_collision(n) == expected_collisions

def test_car_race_collision_zero_cars():
    """Test that the function returns 0 when there are no cars."""
    assert car_race_collision(0) == 0

def test_car_race_collision_negative_cars():
    """Test that the function raises a ValueError when there are a negative number of cars."""
    with pytest.raises(ValueError):
        car_race_collision(-1)

def test_car_race_collision_non_integer_cars():
    """Test that the function raises a TypeError when the number of cars is not an integer."""
    with pytest.raises(TypeError):
        car_race_collision(5.5)