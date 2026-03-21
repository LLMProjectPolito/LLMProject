import pytest

def test_sort_numbers_empty_string():
    assert sort_numbers('') == ''

def test_sort_numbers_single_element():
    assert sort_numbers('one') == 'one'

def test_sort_numbers_already_sorted():
    assert sort_numbers('one two three') == 'one two three'

def test_sort_numbers_unsorted():
    assert sort_numbers('three one five') == 'one three five'

def test_sort_numbers_duplicates():
    assert sort_numbers('one one two') == 'one one two'

def test_sort_numbers_all_numbers():
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'

def test_sort_numbers_invalid_input():
    with pytest.raises(ValueError):
        sort_numbers('ten')

def test_sort_numbers_invalid_input_multiple():
    with pytest.raises(ValueError):
        sort_numbers('ten eleven')

def test_sort_numbers_mixed_case():
    assert sort_numbers('One two Three') == 'two One Three'

def test_sort_numbers_leading_trailing_spaces():
    assert sort_numbers('   one two three   ') == 'one two three'

def test_sort_numbers_multiple_spaces():
    assert sort_numbers('one  two   three') == 'one two three'