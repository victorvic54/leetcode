class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque([])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
        
        if fresh == 0:
            return 0
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = -1
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dir_x, dir_y in dirs:
                    if 0 <= x + dir_x < len(grid) and 0 <= y + dir_y < len(grid[0]) \
                        and grid[x+dir_x][y+dir_y] == 1 and not visited[x+dir_x][y+dir_y]:
                        visited[x+dir_x][y+dir_y] = True
                        fresh -= 1
                        queue.append((x+dir_x, y+dir_y))

        return minutes if fresh == 0 else -1

# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)
