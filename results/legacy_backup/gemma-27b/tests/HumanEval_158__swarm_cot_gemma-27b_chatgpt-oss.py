import pytest

def test_empty_list():
    assert find_max([]) == ""

@pytest.mark.parametrize(
    "words,expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    ],
)
def test_find_max_examples(words, expected):
    assert find_max(words) == expected