class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        memo = {}
        def backtracking(x, y, counter):
            if (x, y, counter) in memo:
                return memo[(x, y, counter)]

            if counter >= maxMove:
                return 0
            
            total = 0
            for dir_x, dir_y in directions:
                if x + dir_x < 0 or x + dir_x >= m or y + dir_y < 0 or y + dir_y >= n:
                    total += 1
                else:
                    total += backtracking(x + dir_x, y + dir_y, counter + 1)

            memo[(x, y, counter)] = total % MOD
            return total % MOD
        return backtracking(startRow, startColumn, 0)

