class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Prim's algorithm
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        pq = [(grid[0][0], (0, 0))]
        while pq:
            w, (x, y) = heapq.heappop(pq)
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return w

            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            for dx, dy in dirs:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    if (x+dx, y+dy) in visited:
                        continue
                    weight = max(w, grid[x+dx][y+dy])
                    heapq.heappush(pq, (weight, (x+dx, y+dy)))
        return -1

# Time: O((V + E) logV)
# Space: O(V)
