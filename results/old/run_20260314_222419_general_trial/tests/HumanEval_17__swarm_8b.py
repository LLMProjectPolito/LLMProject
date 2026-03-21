import pytest
import math
from typing import List

def test_parse_music_empty_string():
    """Test the function with an empty music string."""
    music_string = ''
    result = parse_music(music_string)
    assert result == []

def test_parse_music_single_note_at_start_of_string():
    music_string = '|'
    result = parse_music(music_string)
    assert result == [1]