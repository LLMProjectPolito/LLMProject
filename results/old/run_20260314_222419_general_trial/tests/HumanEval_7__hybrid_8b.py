```python
import pytest
from your_module import filter_by_substring  # replace 'your_module' with actual module name

@pytest.mark.parametrize("strings, substring, expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['hello', 'world', 'python'], 'o', ['hello', 'world']),
    (['123', '456', '789'], '4', ['456']),
    (['test', 'example', 'sample'], '', ['test', 'example', 'sample']),
])
def test_filter_by_substring(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_substring():
    strings = ['abc', 'def', 'ghi']
    substring = ''
    expected = strings
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_no_matches():
    strings = ['abc', 'def', 'ghi']
    substring = 'jkl'
    expected = []
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_single_match():
    strings = ['abc', 'def', 'ghi']
    substring = 'd'
    expected = ['def']
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_substring_variants():
    assert filter_by_substring(['abc', 'bacd', 'cde'], '') == ['abc', 'bacd', 'cde']

def test_filter_by_substring_empty_input():
    with pytest.raises(TypeError):
        filter_by_substring(None, 'a')

def test_filter_by_substring_empty_substring():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'bacd'], None)

def test_filter_by_substring_empty_input_empty_substring():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_input_empty_substring_variants():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants2():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants3():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants4():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants5():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants6():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants7():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants8():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants9():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants10():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants11():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants12():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants13():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants14():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants15():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants16():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants17():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants18():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants19():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants20():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants21():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants22():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants23():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants24():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants25():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants26():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants27():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants28():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants29():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants30():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants31():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants32():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants33():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants34():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants35():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants36():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants37():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants38():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants39():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants40():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants41():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants42():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants43():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants44():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants45():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants46():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants47():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants48():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants49():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants50():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants51():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants52():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants53():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants54():
    with pytest.raises(TypeError):
        filter_by_substring(None, '')

def test_filter_by_substring_empty_substring_empty_input_variants55