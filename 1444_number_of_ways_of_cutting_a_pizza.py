"""
prefix_sum: store the total sum of pizza from position (x,y) to the last position (-1, -1)

Example:
pizza =  A..
         AAA
         .A.

prefix_sum = [5, 3, 1, 0]
             [4, 3, 1, 0]
             [0, 1, 0, 0]
             [0, 0, 0, 0]
"""
class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        MOD = 10 ** 9 + 7

        m, n = len(pizza), len(pizza[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                prefix_sum[r][c] = prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - prefix_sum[r + 1][c + 1] + (pizza[r][c] == 'A')

        memo = {}
        def cut_pizza(k, r, c):
            if (k, r, c) in memo:
                return memo[(k, r, c)]

            if prefix_sum[r][c] == 0:
                return 0
            
            if k == 0:
                return 1

            ans = 0
            # cut horizontally
            for nr in range(r + 1, m):
                if prefix_sum[r][c] - prefix_sum[nr][c] > 0: # can we cut top side (need at least 1 apple)?
                    memo[(k-1, nr, c)] = cut_pizza(k-1, nr, c)
                    ans = (ans + memo[(k-1, nr, c)]) % MOD

            # cut vertically                    
            for nc in range(c + 1, n):
                if prefix_sum[r][c] - prefix_sum[r][nc] > 0: # can we cut left side (need at least 1 apple)?
                    memo[(k-1, r, nc)] = cut_pizza(k-1, r, nc)
                    ans = (ans + memo[(k-1, r, nc)]) % MOD

            return ans

        return cut_pizza(K - 1, 0, 0)
