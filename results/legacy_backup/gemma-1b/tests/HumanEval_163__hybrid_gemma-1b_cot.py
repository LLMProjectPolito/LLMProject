def merge_suites(suite1, suite2):
    """Merges two pytest suites into a single suite."""
    combined_tests = suite1 + suite2
    return combined_tests

if __name__ == '__main__':
    # Example usage:
    suite1 = generate_integers(2, 8)
    suite2 = generate_integers(8, 2)
    merged_suite = merge_suites(suite1, suite2)
    print(merged_suite)

    suite3 = generate_integers(10, 14)
    suite4 = generate_integers(14, 10)
    merged_suite2 = merge_suites(suite3, suite4)
    print(merged_suite2)