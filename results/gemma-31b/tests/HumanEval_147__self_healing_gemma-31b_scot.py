
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    if n < 3:
        return 0
    
    # a[i] = i^2 - i + 1
    # Modulo 3 analysis:
    # i % 3 == 0: a[i] = 0 - 0 + 1 = 1 (mod 3)
    # i % 3 == 1: a[i] = 1 - 1 + 1 = 1 (mod 3)
    # i % 3 == 2: a[i] = 4 - 2 + 1 = 3 = 0 (mod 3)
    # So a[i] is 0 mod 3 if i % 3 == 2, and 1 mod 3 otherwise.
    # a[i] is never 2 mod 3.
    
    # Count of elements where a[i] % 3 == 0
    # i = 2, 5, 8, ... (3k - 1)
    # 3k - 1 <= n  => 3k <= n + 1 => k <= (n + 1) // 3
    c0 = (n + 1) // 3
    
    # Count of elements where a[i] % 3 == 1
    c1 = n - c0
    
    # Count of elements where a[i] % 3 == 2
    c2 = 0
    
    # For (a[i] + a[j] + a[k]) % 3 == 0:
    # Possible combinations of (mod 3) values:
    # 1. (0, 0, 0) -> combinations(c0, 3)
    # 2. (1, 1, 1) -> combinations(c1, 3)
    # 3. (2, 2, 2) -> combinations(c2, 3)
    # 4. (0, 1, 2) -> c0 * c1 * c2
    
    def combinations_3(k):
        if k < 3:
            return 0
        return k * (k - 1) * (k - 2) // 6
    
    return combinations_3(c0) + combinations_3(c1) + combinations_3(c2) + (c0 * c1 * c2)