from typing import List

def parse_music(music_string: str) -> List[int]:
    note_durations = {
        'o': 4,  # whole note
        'o|': 2,  # half note
        '.|': 1   # quater note
    }

    if not music_string:
        raise ValueError("Input string is empty")

    if not all(isinstance(note, str) for note in music_string.split()):
        raise ValueError("Invalid note format")

    notes = music_string.split()

    durations = []

    for note in notes:
        note = note.replace('|', '')

        if note == 'o':
            # 'o' - whole note, lasts four beats
            durations.append(4)
        elif note == 'o|':
            # 'o|' - half note, lasts two beats
            durations.append(2)
        elif note == '.|':
            # '.|' - quater note, lasts one beat
            durations.append(1)
        elif note in note_durations:
            # 'o' or 'o|' or '.|' - use dictionary
            durations.append(note_durations[note])
        else:
            # Invalid note
            raise ValueError(f"Invalid note: {note}")

    return durations

# Testing the function
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
print(parse_music('o o| .| o| o| .| .|. .| .|. .| .|. o o|'))
print(parse_music('o o| .| o| o| .| o o'))