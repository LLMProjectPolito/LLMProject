import pytest

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 3),
    (4, 6),
    (5, 10),
])
def test_car_race_collision(n: int, expected: int):
    assert car_race_collision(n) == expected

@pytest.mark.parametrize("n, expected", [
    (-1, 0),  # negative numbers are not valid inputs
    (0.5, 0),  # non-integers are not valid inputs
    ('a', 0),  # non-integers are not valid inputs
])
def test_car_race_collision_invalid_input(n: int, expected: int):
    with pytest.raises(TypeError):
        car_race_collision(n)

def test_car_race_collision_zero_speed():
    # this test is not possible as the function does not use speed as an input
    pass

def test_car_race_collision_invalid_type():
    with pytest.raises(TypeError):
        car_race_collision("a")  # test for non-integer inputs

def test_car_race_collision_invalid_input_type():
    with pytest.raises(TypeError):
        car_race_collision(1.5)  # test for non-integer inputs

def test_car_race_collision_negative_input():
    with pytest.raises(TypeError):
        car_race_collision(-1)  # test for negative inputs