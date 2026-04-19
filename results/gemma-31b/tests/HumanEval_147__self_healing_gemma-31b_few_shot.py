
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
    # i % 3 == 0 => a[i] = 0 - 0 + 1 = 1 (mod 3)
    # i % 3 == 1 => a[i] = 1 - 1 + 1 = 1 (mod 3)
    # i % 3 == 2 => a[i] = 4 - 2 + 1 = 3 = 0 (mod 3)
    # Let c0 be the count of a[i] % 3 == 0, and c1 be the count of a[i] % 3 == 1.
    # a[i] % 3 == 0 if i % 3 == 2.
    # In the range 1 to n, the number of i such that i % 3 == 2 is (n + 1) // 3.
    
    c0 = (n + 1) // 3
    c1 = n - c0
    
    def comb3(k):
        if k < 3:
            return 0
        return k * (k - 1) * (k - 2) // 6
    
    # A triple (x, y, z) sums to a multiple of 3 if:
    # 1. All three are 0 (mod 3): comb(c0, 3)
    # 2. All three are 1 (mod 3): comb(c1, 3)
    # 3. One is 0, one is 1, one is 2 (mod 3): c0 * c1 * c2 (but c2 is always 0)
    
    return comb3(c0) + comb3(c1)