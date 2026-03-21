import pytest
from typing import List

def parse_music(music_string: str) -> List[int]:
    # implementation of the function
    notes = music_string.split()
    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats

def test_parse_music_whole_note():
    assert parse_music('o') == [4]

def test_parse_music_half_note():
    assert parse_music('o|') == [2]

def test_parse_music_quarter_note():
    assert parse_music('.|') == [1]

def test_parse_music_multiple_notes():
    assert parse_music('o o| .|') == [4, 2, 1]

def test_parse_music_empty_string():
    assert parse_music('') == []

def test_parse_music_multiple_whole_notes():
    assert parse_music('o o') == [4, 4]

def test_parse_music_multiple_half_notes():
    assert parse_music('o| o|') == [2, 2]

def test_parse_music_multiple_quarter_notes():
    assert parse_music('.| .|') == [1, 1]

def test_parse_music_complex_input():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

def test_parse_music_invalid_input():
    with pytest.raises(ValueError):
        parse_music('invalid')

def test_parse_music_invalid_note():
    with pytest.raises(ValueError):
        parse_music('o|o')