
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def merge_suites(suite1, suite2):
    """Merges two pytest suites into a single suite."""
    merged_suite = suite1.union(suite2)
    return merged_suite

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