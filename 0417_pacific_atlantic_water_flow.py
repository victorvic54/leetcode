class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def backtracking(queue):
            canReach = [[False] * len(heights[0]) for _ in range(len(heights))]
            for x, y in queue:
                canReach[x][y] = True

            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in dirs:
                        if 0 <= x + dx < len(heights) and 0 <= y + dy < len(heights[0]) and \
                            heights[x][y] <= heights[x+dx][y+dy] and not canReach[x+dx][y+dy]:
                            queue.append((x+dx, y+dy))
                            canReach[x+dx][y+dy] = True
            return canReach

        pacific_queue = deque([])
        for i in range(len(heights)):
            pacific_queue.append((i, 0))
        
        for j in range(len(heights[0])):
            pacific_queue.append((0, j))

        atlantic_queue = deque([])
        for i in range(len(heights)):
            atlantic_queue.append((i, len(heights[0]) - 1))
        
        for j in range(len(heights[0])):
            atlantic_queue.append((len(heights) - 1, j))
        
        canReachPacific = backtracking(pacific_queue)
        canReachAtlantic = backtracking(atlantic_queue)

        results = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if canReachPacific[i][j] and canReachAtlantic[i][j]:
                    results.append((i, j))
        return results


# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)
