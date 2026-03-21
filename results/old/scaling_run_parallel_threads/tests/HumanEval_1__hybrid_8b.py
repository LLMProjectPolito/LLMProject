import pytest
from your_module import separate_paren_groups  # replace 'your_module' with actual module name

@pytest.mark.parametrize("input_string, expected_output", [
    ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
    ('(()) () ()', ['(())', '()', '()']),
    ('() () ()', ['()', '()', '()']),
    ('', []),
    ('   ', []),
    ('  (  )  ', ['()']),
    ('((()))(())()(()())', ['((()))', '(())', '()', '(()())']),
    ('()', ['()']),
    ('(()) ()', ['(())', '()']),
    ('() () ()', ['()', '()', '()']),
])
def test_separate_paren_groups(input_string, expected_output):
    assert separate_paren_groups(input_string.replace(' ', '')) == expected_output

def test_separate_paren_groups_nested():
    input_string = '(())(())'
    expected_output = ['(())', '(())']
    assert separate_paren_groups(input_string) == expected_output

def test_separate_paren_groups_unbalanced():
    input_string = '(())('
    with pytest.raises(ValueError):
        separate_paren_groups(input_string)

def test_separate_paren_groups_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']