class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(x, y):
            if visited[x][y]:
                return 0
            
            max_count = 1
            visited[x][y] = True
            for dx, dy in dirs:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == 1:
                    max_count += dfs(x+dx, y+dy)
            return max_count
        
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == 1:
                    max_count = max(max_count, dfs(i, j))
        return max_count

# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)
