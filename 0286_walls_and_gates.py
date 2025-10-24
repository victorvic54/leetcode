class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        queue = deque([])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        depth = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                visited[x][y] = True
                grid[x][y] = min(grid[x][y], depth)
                for dx, dy in dirs:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) \
                        and grid[x+dx][y+dy] != -1 and not visited[x+dx][y+dy]:
                        queue.append((x+dx, y+dy))
            depth += 1
        return

# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        # result = [[None] * len(grid[0]) for _ in range(len(grid))]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(pos):
            depth = 0
            queue = deque([pos])
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    visited[x][y] = True
                    grid[x][y] = min(grid[x][y], depth)
                    for dx, dy in dirs:
                        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) \
                            and grid[x+dx][y+dy] != -1 and not visited[x+dx][y+dy]:
                            queue.append((x+dx, y+dy))
                depth += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs((i, j))
        return

# G: number of gates, M: rows, N: columns
# Time: O(G x M x N)
# Space: O(M x N)
