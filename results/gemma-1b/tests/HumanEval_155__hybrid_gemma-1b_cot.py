
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def merge_suites():
    def merge_tests(suite1, suite2):
        """Merges two pytest suites into a single suite."""
        combined_tests = []
        for test_name in suite1:
            test_func = getattr(suite1, test_name)
            if isinstance(test_func, pytest.Func):
                combined_tests.append(test_func)
        for test_name in suite2:
            test_func = getattr(suite2, test_name)
            if isinstance(test_func, pytest.Func):
                combined_tests.append(test_func)
        return combined_tests

    return merge_tests(Suite1, Suite2)

if __name__ == '__main__':
    merged_suite = merge_suites()
    print(merged_suite)