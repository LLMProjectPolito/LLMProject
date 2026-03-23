lst_copy = list(lst)
lst_copy.sort(key=lambda x: (len(x), x))