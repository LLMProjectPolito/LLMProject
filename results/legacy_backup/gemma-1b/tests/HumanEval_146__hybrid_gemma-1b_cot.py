def merge_tests(suite1, suite2):
    """Merges two pytest suites into a single suite."""
    combined_tests = suite1 + suite2
    return combined_tests

if __name__ == '__main__':
    # Example usage:
    suite1 = [specialFilter([15, -73, 14, -15]), specialFilter([33, -2, -3, 45, 21, 109])]
    suite2 = [specialFilter([1, 2, 3, 4, 5]), specialFilter([6, 7, 8, 9, 10])]

    merged_suite = merge_tests(suite1, suite2)
    print(merged_suite)