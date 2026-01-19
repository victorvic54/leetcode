class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix_sum_row = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(1, n + 1):
                prefix_sum_row[i][j] = prefix_sum_row[i][j-1] + mat[i][j-1]
        
        prefix_sum_col = [[0] * (n) for _ in range(m + 1)]
        for j in range(n):
            for i in range(1, m + 1):
                prefix_sum_col[i][j] = prefix_sum_col[i-1][j] + mat[i-1][j]
        
        max_len = 0
        for i in range(m):
            for j in range(n):
                total = 0
                length = 1
                while length <= min(m - i, n - j): # can be optimize using binary search
                    total += prefix_sum_row[i+length-1][j+length] - prefix_sum_row[i+length-1][j]
                    total += prefix_sum_col[i+length][j+length-1] - prefix_sum_col[i][j+length-1]
                    total -= mat[i+length-1][j+length-1]
                    if total > threshold:
                        break

                    max_len = max(max_len, length)
                    length += 1
        return max_len

# Time: O(mn min(m, n))
# Space: O(mn)
