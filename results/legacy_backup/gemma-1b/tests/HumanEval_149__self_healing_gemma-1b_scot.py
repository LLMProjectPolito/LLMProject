import pytest

def list_sort(lst):
    """Sorts a list of strings by length, then alphabetically, and removes strings with odd lengths."""
    return sorted(lst, key=lambda x: (len(x), x))