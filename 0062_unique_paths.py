import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m == 1 or n == 1):
            return 1
        
        tmp_list = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                tmp_list[j] += tmp_list[j - 1]

        return tmp_list[n - 1]
    
    
    # Math way:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))
    