def list_sort(lst):
    """
    Sorts a list of strings by length of each word, and returns the sorted list.
    """
    lst_copy = list(lst)
    lst_copy.sort(key=lambda x: (len(x), x))
    return lst_copy