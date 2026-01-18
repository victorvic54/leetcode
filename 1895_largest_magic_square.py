class Solution:
    def is_magic_sq(self, grid, i, j, length):
        magic_num = None
        for x in range(i, i + length):
            num = sum(grid[x][y] for y in range(j, j + length))
            if magic_num == None:
                magic_num = num
            elif magic_num != num:
                return False
        
        for y in range(j, j + length):
            num = sum(grid[x][y] for x in range(i, i + length))
            if magic_num == None:
                magic_num = num
            elif magic_num != num:
                return False
    
        if sum(grid[i+x][j+x] for x in range(length)) != magic_num:
            return False
        
        if sum(grid[i+x][j+length-1-x] for x in range(length)) != magic_num:
            return False

        return True
    
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        max_len = 1
        m, n = len(grid), len(grid[0])

        tmp_len = 2
        while tmp_len <= min(m, n):
            for i in range(m - tmp_len + 1):
                for j in range(n - tmp_len + 1):
                    if self.is_magic_sq(grid, i, j, tmp_len):
                        max_len = max(max_len, tmp_len)
            tmp_len += 1
        return max_len

# Given N = len square grid
# Time: O(N**5)
