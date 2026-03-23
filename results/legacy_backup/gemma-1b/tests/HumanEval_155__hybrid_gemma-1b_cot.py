def merge_suites(suite1, suite2):
    """Merges two pytest suites into a single suite."""
    combined_tests = suite1 + suite2
    return combined_tests

if __name__ == '__main__':
    # Example usage:
    suite1 = [even_odd_count(12), even_odd_count(234), even_odd_count(-123)]
    suite2 = [even_odd_count(123), even_odd_count(456), even_odd_count(789)]

    merged_suite = merge_suites(suite1, suite2)
    print(merged_suite)