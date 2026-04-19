
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
    # a[i] = i^2 - i + 1
    # a[i] % 3:
    # i % 3 == 0 -> 0 - 0 + 1 = 1
    # i % 3 == 1 -> 1 - 1 + 1 = 1
    # i % 3 == 2 -> 4 - 2 + 1 = 3 = 0
    # So a[i] is 0 mod 3 if i % 3 == 2, else 1 mod 3.
    
    # Count of i in {1, ..., n} such that i % 3 == 2
    c0 = (n + 1) // 3
    # Count of i in {1, ..., n} such that i % 3 == 0 or 1
    c1 = n - c0
    
    # We need a[i] + a[j] + a[k] % 3 == 0.
    # Since a[i] % 3 is only 0 or 1, the only combinations are:
    # (0, 0, 0) or (1, 1, 1).
    
    def nCr3(m):
        if m < 3:
            return 0
        return m * (m - 1) * (m - 2) // 6
        
    return nCr3(c0) + nCr3(c1)