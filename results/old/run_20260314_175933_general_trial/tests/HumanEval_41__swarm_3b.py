import pytest
import math

def test_car_race_collision():
    """Test car_race_collision function with different number of cars."""
    # Test with equal number of cars going left to right and right to left
    assert car_race_collision(1) == 0
    
    # Test that at least 1 collision occurs when there's at least 1 car on each side
    assert car_race_collision(1) == 1
    
    # Test with equal numbers of cars and only one car collision
    assert car_race_collision(2) == 1