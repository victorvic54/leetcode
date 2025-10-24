class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        num_islands = 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(x, y):
            if visited[x][y]:
                return
            
            visited[x][y] = True
            for dx, dy in dirs:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == "1":
                    dfs(x+dx, y+dy)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    num_islands += 1
                    dfs(i, j)
        return num_islands

# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)
