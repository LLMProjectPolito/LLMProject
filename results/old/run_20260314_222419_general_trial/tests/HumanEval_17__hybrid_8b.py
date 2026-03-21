import pytest

@pytest.mark.parametrize("music_string, expected_output", [
    ('o o| .| o| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    ('o| o| o| o|', [2, 2, 2, 2]),
    ('.| .| .| .|', [1, 1, 1, 1]),
    ('o o o o', [4, 4, 4, 4]),
    ('', []),
    ('o', [4]),
    ('o|', [2]),
    ('.|', [1])
])
def test_parse_music(music_string, expected_output):
    assert parse_music(music_string) == expected_output

@pytest.mark.parametrize("music_string, expected_output", [
    ('o', [4]),
    ('o|', [2]),
    ('.|', [1]),
    ('o o|', [4, 2]),
    ('o o| .|', [4, 2, 1]),
    ('o o| .| o|', [4, 2, 1, 2]),
    ('', []),
    ('o o o', [4, 4, 4]),
    ('o| o| o|', [2, 2, 2]),
    ('.| .| .|', [1, 1, 1]),
])
def test_parse_music_additional_cases(music_string, expected_output):
    assert parse_music(music_string) == expected_output

def test_parse_music_invalid_input():
    with pytest.raises(TypeError):
        parse_music(123)

def test_parse_music_empty_string():
    assert parse_music('') == []

def test_parse_music_invalid_characters():
    with pytest.raises(ValueError):
        parse_music('abc')