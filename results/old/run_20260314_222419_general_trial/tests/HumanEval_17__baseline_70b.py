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

def test_parse_music_empty_string():
    assert parse_music('') == []

def test_parse_music_single_whole_note():
    assert parse_music('o') == [4]

def test_parse_music_single_half_note():
    assert parse_music('o|') == [2]

def test_parse_music_single_quarter_note():
    assert parse_music('.|') == [1]

def test_parse_music_multiple_notes():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

def test_parse_music_invalid_note():
    with pytest.raises(ValueError):
        parse_music('x')

def test_parse_music_invalid_input():
    with pytest.raises(TypeError):
        parse_music(123)

def test_parse_music_large_input():
    large_input = 'o ' * 1000
    assert len(parse_music(large_input)) == 1000

def test_parse_music_edge_cases():
    assert parse_music(' ') == []
    assert parse_music('   ') == []