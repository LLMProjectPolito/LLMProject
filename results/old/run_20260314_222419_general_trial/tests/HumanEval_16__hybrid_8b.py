import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ('xyzXYZ', 3),
    ('Jerry', 5),
    ('', 0),
    ('abcABC', 3),
    ('aaaa', 1),
    ('!@#$', 3),
    ('abAB', 2),
    ('123', 3),
    ('!@#', 3),
    ('abc123!@#', 9)
])
def test_count_distinct_characters(input_string, expected_output):
    assert count_distinct_characters(input_string) == expected_output

def test_count_distinct_characters_empty_string():
    assert count_distinct_characters('') == 0

def test_count_distinct_characters_single_character():
    assert count_distinct_characters('a') == 1

def test_count_distinct_characters_same_characters():
    assert count_distinct_characters('aaaaaaaa') == 1

def test_count_distinct_characters_non_alphabetic_characters():
    assert count_distinct_characters('!@#$%^&*()') == 10

def test_count_distinct_characters_case_insensitivity():
    assert count_distinct_characters('aA') == 1

def test_count_distinct_characters_numbers():
    assert count_distinct_characters('123') == 3

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters('!@#') == 3

def test_count_distinct_characters_mixed_input():
    assert count_distinct_characters('abc123!@#') == 9