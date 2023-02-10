"""
Example 1
[1, 0, 1]    [1, 1, 1]    [1, 1, 1]
[0, 0, 0] -> [1, 0, 1] -> [1, 2, 1]
[1, 0, 1]    [1, 1, 1]    [1, 1, 1]

Example 2
[1, 0, 0]    [1, 1, 1]    [1, 1, 1]
[0, 0, 1] -> [1, 1, 1] -> [1, 1, 1]
[0, 0, 0]    [0, 0, 1]    [2, 2, 1]

Explanation:
If you traverse from the sea (grid value = 0), you will get TLE
If you traverse from the land (grid value = 1), return the max value of the grid
"""

from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # land
                    q.append((i, j, 0))
                    
        # if all grid is land or all grid is sea
        if len(q) == 0 or len(q) == len(grid) * len(grid[0]):
            return -1
        
        max_distance = 0
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for i in range(len(q)):
                x, y, distance = q.popleft()
                visited.add((x, y))

                max_distance = max(max_distance, distance)

                for dir_x, dir_y in dirs:
                    newX, newY = x + dir_x, y + dir_y
                    
                    if not(0 <= newX < len(grid) and 0 <= newY < len(grid[0])):
                        continue
                    
                    if (newX, newY) in visited:
                        continue
                    
                    if grid[newX][newY] == 0:
                        q.append((newX, newY, distance + 1))
                        grid[newX][newY] = distance + 1
        return max_distance
